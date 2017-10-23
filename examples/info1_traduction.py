#!/usr/bin/env python

'''
Exemple de solution de l'exercice suivant (de info1.md)
Liste et dictionnaire
On part de la variable de type `liste` nommée couleurs_en

    couleurs_en = ['red', 'blue', 'green', 'pink', 'yellow']

1. Traduction avec stockage de l'information dans deux listes:
    a. Créer une autre variable de type `liste` nommée `couleur_fr` avec pour chaque couleur de la
liste __couleurs_en__ sa traduction en français.
    b. A partir de ces deux listes comme variables d'entrée, écrire un bout de code python permettant de trouver la
traduction en français d'une couleur à partir de la version anglaise d'une couleur.
    b. Transformer le bout de code précédent en une fonction `traduction1`
    c. Quelles sont les désavantages de cette fonction à votre avis ? (vous pouvez utiliser des exemples d'appel à cette
fonction pour illustrer)

2. Traduction avec stockage de l'information dans une liste de listes
    a. Faire la même chose que précédemment mais en utilisant une seule variable d'entrée (de type liste de listes)
    b. Transformer ce bout de code en une fonction `traduction2`

3. Traduction en utilisant un VRAI dictionnaire
    En utilisant un SEUL objet de type `dictionnaire` python (stockant de manière plus intelligente les informations,
    créer une fonction traduction3 qui traduit un mot en anglais en français
'''

def traduction1(couleur_anglais, couleurs_en_anglais, couleurs_en_francais) :
    """Traduit une couleur en anglais en francais.
    Entrées :
    couleur_anglais : string avec la couleur à traduire
    couleurs_en_anglais : liste des noms de couleurs en anglais.
    couleurs_en_français : liste des noms de couleurs en français.

    Sortie : string avec la traduction en français de "couleur_en_anglais"

    Ex :
    > couleur_anglais = 'red'
    > couleurs_en = ['red', 'blue']
    > couleurs_fr = ['rouge', 'bleu']
    > traduction1(couleur_anglais, mes_couleurs_en_anglais, mes_couleurs_en_français)
    Out : 'rouge'
    """
    index_de_la_couleur = couleurs_en_anglais.index(couleur_anglais)
    print("index", index_de_la_couleur)
    couleur_francais = couleurs_en_francais[index_de_la_couleur]
    #print(couleur_anglais, "se traduit par {}.format()")
    print("traduction_en_francais", couleur_francais)
    return(couleur_francais)

def traduction2(couleur_anglais, dico_anglais_francais):
    """Traduit une couleur en anglais en francais.
    Entrées :
    couleur_anglais : string avec la couleur à traduire
    dico_anglais_francais : liste de listes du type [['red','rouge'], ...]
    Sortie :
    string avec la traduction en français de "couleur_en_anglais"

    Ex.:
    dico = [['red','rouge'], ['blue', 'bleu']]
    traduction2('red', dico)
    Out: 'rouge'
    """
    for paire_de_mots in dico_anglais_francais:
        if paire_de_mots[0] == couleur_anglais:
            couleur_francais = paire_de_mots[1]
            print(couleur_francais)
    return couleur_francais


# 1. Traduction avec stockage des informations dans deux listes

## Définition des variables d'entrée
couleurs_en = ['red', 'blue']
couleurs_fr = ['rouge', 'bleu']
couleur = 'rouge'

## Traduction sans fonction:
mon_index = couleurs_fr.index(couleur)
couleurs_fr[mon_index]

## Traduction en utilisant la fonction "traduction1"
traduction1('red', couleurs_en, couleurs_fr)

couleurs_en = [4,3]
traduction1('red', couleurs_en, couleurs_fr)


# 2. Traduction avec stockage des informations dans une liste de listes

## Definition des variables d'entrée
ma_couleur = 'red'
dico = [['red','rouge'], ['blue', 'bleu']]

## Solution sans fonction
for paire in dico:
    if paire[0] == ma_couleur:
        print(paire[1])

## Avec fonction traduction2
ma_couleur_en_francais = traduction2('red', dico)
print('la traduction de red est ', ma_couleur_en_francais )

# 3. Traduction en utilisant un dictionnaire python
vrai_dico = {'red':'rouge', 'blue': 'bleu'}
print(vrai_dico['red']) # pas besoin de créer de fonction !
