import os

directory = os.path.join("C:/Users", "roca", "Documents", "cogmaster2017-info1",
"session3")
os.chdir(directory)

"""
1. Un dictionnaire est-il modifiable ?

Nous avons vu que le tuple n'est pas modifiable.
Testez si c'est le cas pour un dictionnaire.
"""

dico = {'red':'rouge', 'blue': 'bleu'}
print(dico)
dico['red'] = 'vert'
print(dico)

print("Oui un dictionnaire est modifiable.")

"""
2. Nombre de mots d'un texte
Ecrire une fonction qui prend en entrée la variable `texte` et donne en sortie le nombre de mots qu'elle contient.
"""

def nombre_de_mots(un_texte):
    """
    Donne le nombre de mots d'un texte
    :param un_texte: texte sous forme de string
    :return: nombre de mots contenu dans le texte
    """
    liste_des_mots = un_texte.split(' ')
    print(liste_des_mots)
    return(len(liste_des_mots))

def nombre_de_mots_sans_ponctuation(un_texte):
    """
    Donne le nombre de mots d'un texte, en tenant compte
    de la ponctuation et des sauts de ligne.
    :param un_texte: texte sous forme de string
    :return: nombre de mots contenu dans le texte
    """
    un_texte = un_texte.replace('.', '')
    un_texte = un_texte.replace(',', '')
    un_texte = un_texte.replace('\n', ' ')
    un_texte = un_texte.replace('\'', ' \' ')
    liste_des_mots = un_texte.split(' ')

    # nouvelle_liste_de_mots = []
    # for mot in liste_des_mots:
    #     if mot != '' and mot != '\'':
    #         nouvelle_liste_de_mots.append(mot)
    #autre façon plus courte pour faire la même chose :
    nouvelle_liste_de_mots = [mot for mot in liste_des_mots if (mot != '' and mot != '\'')]
    print(nouvelle_liste_de_mots)
    return(len(nouvelle_liste_de_mots))

# Remarque : pour simplifier la suite et éviter la duplication de code,
# on peut créer la fonction "mots_sans_ponctuation" suivante
# Elle pourra être réutilisée dans les fonctions définies ensuite.

def mots_sans_ponctuation(un_texte):
    """
    Donne la liste des mots d'un texte en enlevant la ponctuation
    :param un_texte: texte sous forme de string
    :return: liste des mots contenus dans 'un_texte'
    """
    un_texte = un_texte.replace('.', '')
    un_texte = un_texte.replace(',', '')
    un_texte = un_texte.replace('\n', ' ')
    un_texte = un_texte.replace('\'', ' \' ')
    liste_des_mots = un_texte.split(' ')
    nouvelle_liste_de_mots = [mot for mot in liste_des_mots if (mot != '' and mot != '\'')]
    return nouvelle_liste_de_mots

def nombre_de_mots_differents(un_texte):
    """
    Donne le nombre de mots différents
    :param un_texte: texte sous forme de string
    :return: nombre de mots différents
    """
    liste_des_mots = mots_sans_ponctuation(un_texte)
    set_de_mots = set(liste_des_mots)
    print(set_de_mots)
    return len(set_de_mots)

def occurrence_des_mots(un_texte):
    """
    Donne l'occurrence de l'ensemble des mots d'un texte
    :param un_texte: texte sous forme de string
    :return: dictionnaire qui pour chaque mot donne son nombre d'occurrences dans 'un_texte'.
    """
    dico = {}
    mots = mots_sans_ponctuation(un_texte)
    for mot in mots:
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico

def occurrence_des_mots_from_file(filename, output_filename):
    """
    Calcule l'occurrence de l'ensemble des mots d'un texte
    :param filename: filename of a text file
    :param output_filename: output filename où le dictionnaire
    contenant l'occurrence des mots contenu dans le fichier texte 'filename'
    sera enregistré.
    :return: le dictionnaire associé
    """
    my_file = open(filename, 'r', encoding='utf-8')#iso-8859-1
    contenu = my_file.read()
    my_file.close()
    dico = occurrence_des_mots(contenu)
    with open(output_filename, 'w', encoding = 'utf-8') as fichier:
        fichier.write(str(dico))
    #autre possibilité:
    # print(dico, file=open(output_filename, 'w', encoding = 'utf-8'))
    return dico

texte = """Vous pouvez remplacer ce texte par n\'importe quoi.
Une poésie, un article de journal, des mots aléatoires ou autres.
Vous pouvez aussi ne pas modifier ce texte. L\'important est que la valeur de la variable \'texte\' soit bien une chaîne de caractère.
"""

print('nombre de mots:', nombre_de_mots(texte))
print('nombre de mots sans ponctuation:', nombre_de_mots_sans_ponctuation(texte))
print('nombre de mots différents:', nombre_de_mots_differents(texte))
print('occurrence des mots', occurrence_des_mots(texte))

mes_occurrences = occurrence_des_mots_from_file('mon_texte.txt', 'resultat2.txt')
print('a partir d\'un texte : ', mes_occurrences)
