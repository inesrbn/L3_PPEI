# Le langage de balisage Markdown

Ce document est écrit selon la syntaxe Markdown, c'est un simple fichier texte avec quelques balises ou caractères spéciaux qui sont interprétées pour la structure et la mise en page.
Par exemple, la première ligne commence par `# ` et représente un titre de niveau 1 (titre principal).
Et dans la phrase précédente, on utilise deux _backquotes_ pour encadrer du code source.
Et juste précédemment, on a utilise `_` pour mettre un passage en italique.
Attention, on va changer de paragraphe, juste en sautant une ligne.

Markdown est très facile a apprendre et rapidement très naturel à utiliser.
On le rencontre très souvent dans les dépôts `git` pour les fichiers d'information `README.md`, ou même dans la documentation embarquée dans le code source qui est ensuite utilisée pour générer les manuels de référence.
Il est aussi beaucoup utilisé pour prendre des notes, écrire des pages web, etc.
En effet, il est facile à partir d'un fichier Markdown de générer du HTML ou d'autres formats (comme du LaTeX).

## Références sur Markdown

Il existe beaucoup de documentation en ligne sur Markdown, en particulier:

* [Markdown guide](https://www.markdownguide.org) un guide assez complet
* [Définition de référence](https://daringfireball.net/projects/markdown/)
* [La page Wikipedia](https://fr.wikipedia.org/wiki/Markdown) avec un guide succinct en français

Vous aurez remarqué au passage ci-dessus:

 * un titre de niveau 2 avec `## `
 * des liens avec `[texte](url)`
 * des listes à puces comme celle-ci

## Petit tour d'horizon

 * les titres de `# ` à `##### `
 * les listes a puces (on y est)
    1. et les listes numérotées
    1. on voit qu'on peut les imbriquer
    1. et qu'on n'a pas besoin de mettre des numéros valides
 * _l'italique_
 * **le gras**
 * [les liens](...)
 * les paragraphes (vus ci-dessus)
 * le `code source`
 * les blocs de code source

```python
def function():
    print("Hello from Python")
```
