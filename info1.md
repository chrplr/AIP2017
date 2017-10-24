---
title: "Introduction to programming in  Python"
author: "Pauline Roca"
date: "21 September, 2017"
output:
  tufte::tufte_handout: default
  tufte::tufte_html: default
---

## Sommaire

**Session 1 et 2:**
  * [Manipuler du texte en python](#manipuler-du-texte-en-python) :
  Type `string` ou `chaîne de caractères`, notion d'`itérable` et accès
aux éléments, boucle `for`, formater des chaînes de caractères

  * [Rappel sur les listes et limitations](#rappel-sur-les-listes-et-limitations) : `listes`, méthode `index`, parcours des éléments d'une liste avec
 boucle `for` et fonction `enumerate`

     Exercice de traduction : faire des fonctions en utilisant les types définis précédemment.
 Notion de `return`

  * [Les dictionnaires](#les-dictionnaires) : Type `dictionnaire`, notion de paire `clé:valeur`

**Session 3 :**
  * [Exercices sur l'occurrence des mots d'un texte](#exercices) : type `set`, opérateur logique `and` dans structure conditionnelle `if`,

Révision : création et appel de fonctions, boucle for

Débug à l'exécution en lançant le script avec
 une console Anaconda.

**Session 4 :**
  * [Manipulation de fichiers texte en python](#manipulation-de-fichiers-texte-en-python) : ouverture, lecture, écriture
  * [Introduction à la notion de test et de "test-driven development"](#introduction-à-la-notion-de-test-et-de-test-driven-development)
  * [Séance de développement orienté "test" (test-driven)](#séance-test-driven-development)


# Manipuler du texte en python
```
import turtle
turtle.pencolor('red')
type('red')
```

Un texte est un type de données en python, appelé `string`.

Un ensemble de caractères stockés les uns à la suite des autres : `une chaîne de caractères`.

On peut le stocker dans une variable :

    color = "red"

Affichage :

    print(color)

C'est une `séquence` de caractères, chaque caractère étant accessibles comme dans une liste :

-----------------
**Exo. Une séquence de caractères**

1. Afficher séquentiellement toutes les lettres du mot "red" à l'aide d'une boucle `for`
2. Afficher la première lettre du mot
3. Afficher les deux premiers caractères
4. Qu'est-ce qui se passe si on essaie de changer un caractère ?

**Solution**

```
    color = "red"
    for c in color:
        print(c)

    print(color[0])
    print(color[1])
    print(color[0:2])
    color[1]=3
```
Un objet `immuable` est un objet dont l'état ne peut pas être modifié après sa création.
Les chaînes de caractères sont `immuables`, comme les tuples.

-----------------

Trouver le nombre de lettres:

    print(len(color))

Deux types de guillemets sont possibles :

    color = 'red'

Des "triples guillemets" peuvent aussi être utilisés pour écrire plusieurs lignes de texte.

    introduction = """Introduction :
    Les chaînes de caractères peuvent aussi être écrites
    sur plusieurs lignes avec des triples quotes"""
    print(introduction)

On peut utiliser aussi des caractères spéciaux:
`\n` permet de passer à la ligne par exemple.

    print("ligne1\nligne2")

On peut aussi concaténer deux chaînes de caractères:

    print('Bonjour, '+ 'ça va bien?')
    print('Je m'appelle Pauline')
    print('Je m\'appelle Pauline')

La même chose en utilisant des variables :

    salut = 'hello world '
    point_d_exclamation = '!'
    print(salut + point_d_exclamation)

------
__Exo optionnel__
Ecrire `Je dors bien.` en utilisant les variables suivantes :

    sujet = 'je'
    verbe = 'dors'
    adverbe = 'bien'
    point = '.'

et la fonction `print`

__Solution__

    print(sujet + verbe + adverbe + point)
    print(sujet +' ' + verbe + ' ' + adverbe + ' ' +point)
    print(sujet, verbe, point, sep=' ')
    print(sujet, verbe, adverbe, sep=' ', end='.')

--------

Ex. Créer une chaîne de caractère avec des entiers
Créer la chaîne de caractère suivante :
`Dans mon placard, j'ai 10 chemises!`
en utilisant les deux variables suivantes :

    nombre_de_chemises = 10

1. Essayer avec l'opérateur `+`. Que constatez-vous ?
2. Essayer avec la méthode  `format`

Solutions.

    sol1 = 'Dans mon placard, j\'ai ' + nombre_de_chemises + '!'
    print(sol1)
    sol2 = 'Dans mon placard j\'ai {} chemises!'.format(nombre_de_chemises)



--------

# Rappel sur les listes et limitations
On peut mettre des chaînes de caractères dans des listes ou des tuples.

Exemple des carrés concentriques dans turtle, où chaque carré avait une couleur :

    couleurs = ['red', 'blue', 'green', 'pink', 'yellow']

Une liste est un ensemble ordonné indicé d'éléments.

    print(couleurs[0])

L'`indice` ou `index` du premier élément est `0`.
Il est associé à une valeur, la chaîne de caractère `red` ici.

## Affichage des éléments d'une liste

    print(couleurs)


## Parcours d'une liste

**Boucle for**

    for couleur in couleurs:
        print(couleur)

**Question :
Comment savoir pendant qu'on parcourt la liste, quel index est associé à la valeur parcourue ?**

**Méthode `index`**

    for couleur in couleurs:
        print(couleur, couleurs.index(couleur))

**Fonction `enumerate`**
La fonction `enumerate` est pratique, et permet de parcourir une liste en itérant sur les paires (index, valeur) :

    for index, couleur in enumerate(couleurs):
        print(index, color)

-------
## Exercice. Liste, texte et dictionnaire
On part de la variable de type `liste` nommée couleurs_en

    couleurs_en = ['red', 'blue', 'green', 'pink', 'yellow']

1. Créer une autre variable de type `liste` nommée `couleur_fr` avec pour chaque couleur de la liste __couleurs_en__ sa traduction en français.
2. A partir de ces deux listes, écrire un bout de code python permettant de trouver la traduction en français d'une couleur à partir de la version anglaise d'une couleur.
3. Transformer le bout de code précédent en une fonction `traduction1`
4. Quelles sont les désavantages de cette fonction à votre avis ? (vous pouvez utiliser des exemples d'appel à cette fonction pour illustrer)
5. Faire la même chose que précédemment mais en utilisant une seule variable (liste de listes par ex.)
6. Transformer ce bout de code en fonction

**Solutions** (solution complète dans
[./examples/info1_traduction.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_traduction.py))


En créant deux listes et en utilisant la méthode `index`.
```
    couleurs_en = ['red', 'blue', 'green', 'pink', 'yellow']
    couleurs_fr = ['rouge', 'bleu', 'vert', 'rose', 'jaune']
    couleur_en = 'red'
    index = couleurs_en.index(couleur_en)
    print(couleurs_fr[index])

    #avec deux tuples:
    tuple_couleurs_en = ('red', 'blue', 'green', 'pink', 'yellow')
    tuple_couleurs_fr = ('rouge', 'bleu', 'vert', 'rose', 'jaune')
    tuple_index = tuple_couleurs_en.index('red')
    print(tuple_couleurs_fr[tuple_index])
```

Avec une fonction:

    def traduction_avec_deux_iterables(couleur_en_anglais, couleurs_fr , couleurs_en):
        index = couleurs_en.index(couleur_en_anglais)
        couleur_en_francais = couleurs_fr[index]
        return couleur_en_francais


**Attention** Et si on change l'ordre des éléments d'une des listes ? (exemple méthode `sort`)

En créant une seule liste de listes :
Aide : pourquoi la méthode `index` ne marche pas ?
Utiliser la fonction `enumerate` et condition `if`

```
dico_couleurs = [['red', 'rouge'], ['blue', 'bleu'], ['green', 'vert'], ['pink', 'rose'], ['yellow', 'jaune']]
couleur_en = 'red'
#dico_couleurs.index(couleur_en)
for index, valeur in enumerate(dico_couleurs):
    if couleur_en == valeur[0]:
        print(valeur[1])
```

ça marche !

```
def traduction_en_français(couleur_en_anglais, dictionnaire_de_couleurs):
    """
    Donne la traduction française d'une couleur à partir du mot en
    anglais et d'un dictionnaire

    Entrées:
    couleur_en_anglais: couleur en anglais (de type string)
    dictionnaire_de_couleurs: liste de listes contenant un ensemble
    de couleurs en anglais associées à leur traduction en français.
    Ex: dictionnaire_de_couleurs = [['red', 'rouge'], ['blue', 'bleu']]

    Sorties:
        traduction en français ou "La couleur n'est pas dans le dictionnaire"
        si la couleur n'est pas présente dans dictionnaire_de_couleurs
    """
    for indice, dico_valeur in enumerate(dictionnaire_de_couleurs):
        if couleur_en_anglais == dico_valeur[0]:
            return dico_valeur[1]
            break
    return "La couleur n'est pas dans le dictionnaire"

dico_couleurs = [['red', 'rouge'], ['blue', 'bleu'], ['green', 'vert'], ['pink', 'rose'], ['yellow', 'jaune']]
traduction_en_français('green', dico_couleurs)
dico_tuple_couleurs = (('red', 'rouge'), ('blue', 'bleu'), ('green', 'vert'))
traduction_en_français('red', dico_tuple_couleurs)
```


Mais solution pas optimale car pour faire un test d'appartenance, on a dû parcourir l'ensemble de la liste !

Finalement, pour répondre à la question posée, on a défini :
  * un objet assez complexe : une liste de liste de deux éléments
  contenant le terme anglais et sa traduction en français, qu'on a mis dans la variable
  `dico_couleurs`
  * une façon de traduire un mot anglais ('red' par ex) en français
  à partir de   `dico_couleurs` et de la fonction `traduction_en_francais`

En python et en programmation dite orientée `objet`, pour pouvoir
créer et réutiliser facilement cet ensemble Objet + fonction, on peut définir
un nouveau type d'objet, appelé `dictionnaire` par exemple, auquel on va
 rajouter une méthode pour rechercher les éléments.
Les développeurs de python ne s'en sont pas privés... Un objet de type
 `dictionnaire` existe déjà !

(pour une introduction à la programmation orientée objet :
[cours openclassrooms sur la notion d'objet](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/notre-premier-objet-les-chaines-de-caracteres))

 Conseil : quand on commence à faire des choses compliquées, bien chercher si
 des outils (objects, focntions, méthodes) n'existent pas déjà, pour éviter
 de ré-inventer la roue !

# Les dictionnaires

## A la recherche d'un dictionnaire dans Turtle...

En utilisant turtle.Screen() et les méthodes associées à l'object créé avec cette fonction :

 * créer une fenetre de largeur et de hauteur égales à 300 pixels
 * Changer la couleur de cette fenetre
 * Quels sont les types des éléments manipulés pour réaliser ces opérations ?
 * Quel est le titre de cette fenêtre ?
 * Comment pensez-vous qu'il est défini ?

 (En vous servant de la documentation (.??), vous pouvez trouver dans le code source où est défini le titre par
défaut)

    fenetre = turtle.Screen()
    fenetre.setup(width=300, height=300, startx=0, starty=0)
    fenetre.bgcolor('red')
    print(type(fenetre)) # turtle._Screen
    print(type(fenetre.bgcolor)) # method
    print(type(fenetre.bgcolor()) # str

La variable `fenetre` est un objet turtle appelé `_Screen` qui a :
- un ensemble de caractéristiques appelées `attributs`
- des méthodes pour interagir avec ces caractéristiques
`fenetre = turtle.Screen()` utilise la fonction Screen de turtle pour créer un object de type `fenêtre` ou `turtle._Screen`

`fenetre??`
Affiche le code source de la définition de ce qu'est une fenêtre
 * les attributs et leur initialisation en premier
 * les méthodes ensuite
```
    __title =_CFG["title"]
    turtle._CFG
```
`turtle._CFG` : Objet qui configure certains paramètres dans turtle

**De quel type il s'agit ?**

    type(turtle._CFG) #dict

Autre ex :

    turtle.pen()

## Qu'est-ce qu'un dictionnaire ?

Une `liste`: ens. ordonné indicé d'éléments.
Objet contenant d'autres objets : un conteneur
Acces aux objets contenus: indices (position)

`Dictionnaire`. conteneur aussi. pas ordonné
accès aux objets contenus: par des `clés`

    pendict = turtle.pen()
    pendict
    pendict["pencolor"]  #black

Creation d'un dictionnaire:

    dico = {}
    type(dico)
    dico["python"] = "grand serpent constricteur"

Si la clé n'existe pas, elle est ajoutée au dictionnaire avec la valeur spécifiée après le signe=.
Sinon, l'ancienne valeur à l'emplacement indiqué est remplacée par la nouvelle.

    dico["python"] = "langage de programmation informatique"


Création de dictionnaires déjà remplis:

    placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

Autre manière de créer un dictionnaire, à partir d'une liste de tuples:

    elements_du_placard = [("chemise", 3), ("pantalon", 6), ("tee-shirt", 7)]
    placard = dict(elements_du_placard)
    print(placard)

iterable, méthode de parcours:

    for cle in placard:
        print(cle)

Parcours des cles:

    for cle in placard.keys():
        print(cle)

Parcours des valeurs:

    for valeur in placard.values():
        print valeur

Parcours des clés et valeurs simultanément (comme enumerate pour les listes)

    for cle, valeur in placard.items():
        print("La clé", cle , "contient la valeur", valeur, sep = " ")


Effacer des éléments :

    placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
    del placard["chemise"]

    placard = {"chemise":3, "pantalon":6, "tee shirt":7}
    placard.pop("chemise")

# Exercices

1. Faire la traduction des couleurs avec un vrai dictionnaire :

A l'aide d'un object de type dictionnaire, écrire un bout de code qui effectue la traduction des 'red', 'blue', 'green', 'pink', 'yellow' en français. Le transformer en fonction.

2. Un dictionnaire est-il modifiable ?

Nous avons vu que le tuple n'est pas modifiable.
Testez si c'est le cas pour un dictionnaire.

-------------------------

3. Nombre de mots d'un texte

```
texte = """Vous pouvez remplacer ce texte par n\'importe quoi.
Une poésie, un article de journal, des mots aléatoires ou autres.
Vous pouvez aussi ne pas modifier ce texte. L\'important est que la valeur de la variable \'texte\' soit bien une chaîne de caractère.
"""
```

Ecrire une fonction qui prend en entrée la variable `texte` précédente et donne en sortie le nombre de mots qu'elle contient.

  * Dans un premier temps ne vous préoccupez pas de la ponctuation (chaque ensemble de caractères compris entre deux caractères ` ` (espace) compte
pour un mot).

Indice : Utiliser la méthode `split` s'appliquant aux chaînes de caractères.

  * Pour enlever la ponctuation, vous pouvez utiliser la méthode  `replace` des chaînes de caractères.

--------------------

4. Ecrire une fonction qui prend en entrée la variable `texte` de l'exercice 3 et donne en sortie le nombre d'occurences de chaque mot qu'elle contient.

N.B. : dans un premier temps, ne faites pas forcément de fonction mais des  tests en ipython

Indices :  Utiliser un dictionnaire pour stocker les informations que
vous mettrez à jour au fur et à mesure

Vous pouvez utiliser : la méthode `split`, une boucle `for` et une structure conditionnelle de type `if ... else `.

------------------


5. Calculer l’occurrence des mots à partir d’un fichier texte, et enregistrer le résultat dans un fichier texte.

Faire une fonction :

qui prend  en entrée le nom d’un fichier texte(i.e. le chemin vers ce fichiers sur votre ordi, exemple : ‘/home/roca/Documents/toto.txt’ pour le fichier toto.txt se trouvant dans mes Documents)

qui donne en sortie le nombre d’occurrences de chaque mot du texte contenu dans le fichier d’entrée, et stocke ces informations dans un nouveau fichier texte.

(regarder dans le cours d’Openclassroom le cours sur les fichiers peut vous aider).

Exemples d'étapes à suivre :
  * Créer un fichier texte avec Atom et enregistrez-le.
  * Ouvrir ce fichier texte en utilisant la fonction `open`
de python
  * En python, lire le contenu de ce fichier en utilisant la méthode `read` et stocker ce contenu dans une variable.
  * A partir de cette variable, vous pouvez maintenant appliquer la fonction que vous avez faite à l’exercice 4.
  * Enregistrer le résultat dans un nouveau fichier texte avec la fonction `write` ou `print`


------------------

6. Dictionnaire et références

Comme les listes, est-ce que le dictionnaire utilise des références ?
En quoi le code suivant vous permet de répondre à cette question ?

    placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
    dressing = placard
    dressing["chemise"] = 4
    print("dressing", dressing)
    print("placard", placard)

(ce chapitre d'openclassroom peut vous aider:
https://openclassrooms.com/courses/apprenez-a-programmer-en-python/portee-des-variables-et-references)

**Correction de l'exercice sur l'occurence des mots (Exos 3-5):**
La solution trouvée en classe dans
[./examples/info1_occurrence_des_mots_en_classe.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_occurrence_des_mots_en_classe.py)
et une autre solution dans [./examples/info1_occurrence_des_mots_autre_correction.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_occurrence_des_mots_autre_correction.py)

**Correction des autres exercices:**
[info1-notebook.ipynb](https://github.com/chrplr/AIP2017/tree/master/info1-notebook.ipynb)


# Manipulation de fichiers texte en python

Vous trouverez dans [./examples/info1_fichiers_texte_lecture_ecriture.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_fichiers_texte_lecture_ecriture.py)
des exemples de manipulation des fichiers texte avec python que l'on a
fait en classe :
  * lecture avec `open` et `close`
  * les différents mode d'ouverture d'un fichier
  * un exemple de changement d'`encodage`
  * ouverture avec `with`
  * écriture avec `write` ou `print`
Pour aller plus loin, j'y ai aussi mis des exemples d'utilisation de :
  * exemple d'écriture d'un fichier `csv` avec `print` et l'argument `sep`
  * idem avec `pandas`
  * `pickle` pour écrire un dictionnaire

Dans [./examples/info1_pandas_example.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_pandas_example.py)
vous trouverez un exemple de code qui manipule les fichiers en python
avec le module `pandas` :
  * lecture d'un fichier excel
'info1_pandas_example_input.xlsx' contenant pour un ensemble de sujets
appartement à deux groupes différents,
l'âge de chacun des sujets (3 colonnes : 'identifiant', 'groupe', 'âge').
  * calcul de la  moyenne des âges des sujets pour chaque groupe
  * écriture de ces informations dans un fichier `csv`
(https://fr.wikipedia.org/wiki/Comma-separated_values) ou `excel` de
sortie.

# Introduction à la notion de test et de "test-driven development"

## Remarques sur la manière d'écrire du code (de développer) :
Pour coder la fonction qui compte l'occurrence des mots d'un texte en entrée
(exercices 3-6),
 il a fallu dans le fichier python [info1_occurrence_des_mots_en_classe.py](https://github.com/chrplr/AIP2017/tree/master/examples/info1_occurrence_des_mots_en_classe.py):
  * décomposer le problème en plusieurs étapes (rôle du découpage en 3
  sous-exercices):
    * compter le nombre de mots (fonction `comptage`)
    * compter le nombre de mots différents (fonctions
     `comptage_mots_differents` et `comptage_dico`)
    * compter l'occurrence de chaque mot (fonction `occurrence_mots`)

  * faire souvent des tests pour vérifier que la fonction créée
 remplissait bien son rôle à chaque étape de l'écriture de cette fonction.
Pour cela, nous avons :
    * créé des exemples de texte où compter l'occurrence des mots, au fur
   et à mesure de notre réflexion, pour vérifier le comportement de la
    fonction dans certains cas précis :
    ```
        texte = """Vous pouvez remplacer ce texte par n\'importe quoi.
        Une poésie, un article de journal, des mots aléatoires ou autres.
        Vous pouvez aussi ne pas modifier ce texte. L\'important est que la valeur de la variable \'texte\' soit bien une chaîne de caractère.
        """
        texte2 = """ Les pigeons se moquent de mon chat """
        texte3 = "la la la la"
        texte_court = "bonjour ça va va"
    ```
    * mis des `print` à l'intérieur des fonctions que l'on voulait
    tester
    * fait ensuite des appels à la fonction avec ces variables:
    ```
        comptage(texte)
        comptage(texte2)
        comptage_mots_differents(texte)
        comptage_mots_differents(texte2)
        comptage_mots_differents(texte3)
        comptage(texte3)
        comptage_dico(texte3)
        occurrence_mots(texte_court)
    ```
    * ouvrir une console Anaconda et exécuter le script
  console Anaconda
    * vérifier visuellement en contrôlant l'affichage (associé aux `print`)
    que la fonction qu'on testait faisait bien `ce qu'on attendait d'elle`

## Avantages de faire des tests manuels
  * Tester en mode "Debug" avec la console Anaconda, nous a permis de
  vérifier sur un(des) cas concret(s) le comportement de notre fonction à l'exécution
  de celle-ci et de corriger au fur et à mesure les éventuels erreurs

  * pour chaque test effectué, nous avons dans le code l'historique des
exemples de textes d'entrée que nous avons testés (" Les pigeons se moquent de mon chat ",
"la la la la", "bonjour ça va va", etc).

## Inconvénients/Problèmes éventuels reliés à cette manière de coder:

  * un peu fastidieux de vérifier visuellement à chaque exécution que
  la fonction testée fait bien ce que l'on veut.
  * d'autant plus qu'il faut bien vérifier que la fonction donne ce que
  l'on veut pour  l'ensemble des tests précédemment effectués (en plus du test en cours)

En effet : On a fait un premier test en appelant la fonction avec un premier texte.
On modifie ensuite la fonction pour l'adapter à un second texte d'entrée.
Rien ne nous dit que les modifications que l'on fait pour s'adapter au
second exemple de texte d'entrée ne vont pas modifier le comportement
de notre fonction avec le premier texte. Il faut donc le re-vérifier.

 * la notion de `la fonction donne ce que l'on veut` n'est pas présente
  dans le code : pour chaque test de fonction effectué, nous avons dans le code les
  textes d'entrée testés  mais pas d'historique sur le comportement
  attendu de la fonction testée car nous avons vérifié de manière visuelle
  `ce qu'on attendait d'elle`.
  Du coup quand on reviendra sur cette fonction dans quelques mois ou
  que quelqu'un reprendra notre code, ce ne sera peut-être plus très clair...


Solution pour mieux faire ? Faire du test-driven en utilisant des outils
adaptés !

# Séance test-driven development

## Liens utiles:

 * bonnes pratiques de programmation en python:
 https://openclassrooms.com/courses/apprenez-a-programmer-en-python/de-bonnes-pratiques
 * tests: https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-tests-unitaires-avec-unittest

