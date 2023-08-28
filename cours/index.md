# PPEI L3

PPEI = Projet Personnel d'Études et d'Insertion

## Qu'est-ce qu'on va faire?

Des trucs utiles quand on fait de l'informatique et valorisables sur un CV (_insertion_):
 * avec une large autonomie (_personnel_)
 * en groupes (ça aussi c'est utile)
 * sous forme de _projet_ (surtout au niveau de la gestion de la collaboration)

Les trucs en question:
 * **Markdown:** un langage de balisage léger et portable, de plus en plus utilisé et de façon très diverse, pas seulement en informatique
 * **git:** un système de contrôle de versions pour gérer l'évolution d'un projet informatique (mais pas seulement) en traçant toutes les modifications des fichiers
 * **LaTeX:** un langage de balisage sophistiqué pour éditer des documents soignés, c'est un traitement de texte complet

## Évaluation

Il faudra constituer des groupes de 3 à 4 personnes, chaque groupe devra préparer un rapport et un exposé sur un sujet libre en informatique (au sens large).
Le fond importe peu, faites vous plaisir, ce qui compte le plus c'est la méthode de rendu et les fichiers produits:
 * créez un compte sur [`codeberg.org`](https://codeberg.org) (un par personne)
 * envoyez vos informations (login, etc.) [sur ce formulaire](https://forms.gle/qwNAZ2dsTSk6WM7K8)
 * je vous inscris à un dépôt `PPEI-L3-[année]` sur `codeberg`
 * vous devez y faire trois contributions
   1. ajout de fichiers, édition Markdown
   2. modification d'un rapport LaTeX
   3. modification d'une présentation LaTeX
 * puis vous présenterez votre exposé à la classe

Cela vous fera quatre notes:
 * une par rendu (respect des procédures avec git, qualité des fichiers)
 * une pour l'exposé (qualité de la présentation)

Tout ceci est détaillé dans le fichier `README.md` à la racine du projet `PPEI-L3-[année]`.

Le calendrier des rendus sera donné en cours.

## Markdown

Détails:
 * le fichier `markdown.md`
 * les liens vers les sites de référence

## git

 * **la base:** un logiciel en ligne de commande
   * ne fait que la gestion des versions
   * plus la communication avec des dépôts
     * copie du projet avec les information sur les versions
     * dans un répertoire ou sur un serveur
 * **les plugins:** des extensions au logiciel de base
   * pour ajouter des fonctionnalités ou des facilités
   * souvent installés par défaut
 * **les serveurs:** pour héberger des dépôts git
   * et permettre leur accès à distance (envoyer ou recevoir des changements)
   * faciliter la collaboration
   * note: cela réduit le besoin en sauvegardes
 * **les forges:** interfaces web sophistiquées ajoutant des fonctionnalités:
   * _bugs trackers_ (avec système de tickets)
   * wiki (pages hypertextes collaboratives)
   * distribution de _releases_/_packages_
   * collaboration avancée (_pull requests_)
   * pages web des projets
   * etc.

   Les plus connues sont `GitHub` (Microsoft) et `GitLab` (open source)

On va surtout voir la ligne de commande et utiliser la forge `codeberg.org` (open source) qui ressemble beaucoup à `GitHub` en plus simple.

Détails: le notebook `git/git.ipynb` ou son rendu HTML `git/git.html`

## LaTeX

Détails: `latex.pdf` (diapos d'un cours fait à l'école doctorale, on n'en verra pas tout)
