import sys

ESC = {"<TAB>": "\t",
       "<NL>": "\n"}

text = sys.stdin.read()
for old, new in ESC.items():
    text = text.replace(old, new)

sys.stdout.write(text)
