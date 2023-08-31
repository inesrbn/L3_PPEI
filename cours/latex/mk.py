import argparse, inspect, ast, shlex, re

from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from tempfile import TemporaryDirectory
from subprocess import run
from shutil import copyfile
from hashlib import sha256
from typing import get_origin
from glob import glob

def lit(src):
    try:
        return ast.literal_eval(src)
    except:
        return src

@dataclass
class Compiler:
    base: Path
    uniq: Path
    pyg: bool = True
    tpl: Optional[str] = None
    pdf: bool = True
    lang: str = "latex"
    dedent: bool = True
    textwidth: Optional[str] = None
    obeylines: bool = False
    latex: tuple[str, ...] = ("latexmk", "-pdflua")
    files: tuple[str, ...] = ()
    @classmethod
    def run(cls, base):
        base = Path(base).with_suffix("")
        opt = base.with_suffix(".opt").read_bytes()
        h = sha256(opt 
                   + b"\0"
                   + base.with_suffix(".src").read_bytes()).hexdigest()
        uniq = base.parent / h
        comp = cls(**cls.parse_opt(base, uniq, opt.decode("utf-8")))
        comp.make_pyg()
        comp.make_pdf()
        comp.make_out()
    @classmethod
    def parse_opt(cls, base, uniq, text) -> dict:
        opt = {"base": base, "uniq": uniq}
        for kv in text.split(","):
            k, v = (s.strip() for s in kv.split("="))
            if get_origin(cls.__dataclass_fields__[k].type) is tuple:
                v = tuple(lit(s) for s in shlex.split(v))
            else:
                v = lit(v)
            opt[k] = v
        return opt
    def make_pyg(self):
        if not self.pyg or self.uniq.with_suffix(".pyg").exists():
            return
        from pygments import highlight
        from pygments import lexers
        from pygments.formatters import LatexFormatter
        code = self.base.with_suffix(".src").read_text()
        if self.dedent:
            code = inspect.cleandoc(code)
        Lexer = lexers.find_lexer_class_by_name("latex")
        with self.uniq.with_suffix(".pyg").open("w") as out:
            out.write(highlight(code, Lexer(), LatexFormatter()))
    def make_pdf(self):
        if not self.pdf or self.uniq.with_suffix(".pdf").exists():
            return
        src = self.base.with_suffix(".src").read_text()
        if self.tpl is not None:
            src = self.make_tex(src)
        if self.obeylines:
            src = src.replace("\\begin{document}", "\\begin{document}\\obeylines", 1)
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            with (tmp / "source.tex").open("w") as tex:
                tex.write(src)
            for pat in self.files:
                for res in glob(pat):
                    tgt = tmp / res
                    tgt.parent.mkdir(parents=True, exist_ok=True)
                    copyfile(res, tgt)
            try:
                run(self.latex + ("-interaction=scrollmode", "source"),
                    cwd=tmpdir, check=True)
                err = None
                if self.tpl is not None and self.tpl.endswith("-crop"):
                    run(["pdfcrop", "--hires", "source.pdf", "cropped.pdf"],
                        cwd=tmpdir, check=True)
                    copyfile(tmp / "cropped.pdf", tmp / "source.pdf")
            except Exception as e:
                err = e
            for ext in (".tex", ".pdf"):
                if (new := tmp / f"source{ext}").exists():
                    old = self.uniq.with_suffix(ext)
                    old.unlink(missing_ok=True)
                    copyfile(new, old)
            if err is not None:
                self.base.with_suffix(".err").write_text(f"{self.uniq}\n")
                raise err
    def make_tex(self, tex):
        tpl = (self.base.parent / f"tpl-{self.tpl}.tex").read_text()
        if self.dedent:
            tpl = inspect.cleandoc(tpl)
        subst = {"TEX": tex.strip()}
        for k in self.__dataclass_fields__:
            subst[k.upper()] = str(getattr(self, k))
        for key, val in subst.items():
            for match in re.finditer(f"\\{{\\{{(.*?)\\b{key}\\b(.*?)\\}}\\}}", tpl):
                tpl = tpl.replace(match.group(0), f"{match.group(1)}{val}{match.group(2)}")
        return tpl
    def make_out(self):
        name = self.base.stem[4:]
        with self.base.with_suffix(".out").open("w") as out:
            out.write(f"\\expandafter\\gedef\\csname pyg:{name}"
                      f"\\endcsname{{{{{self.uniq}.pyg}}}}\n")
            out.write(f"\\expandafter\\gedef\\csname pdf:{name}"
                      f"\\endcsname{{{self.uniq}.pdf}}\n")

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("base", help="base name of the files to be proceeded")
    args = parser.parse_args()
    Compiler.run(args.base)
