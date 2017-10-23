# VERSION FAITE EN CLASSE

def comptage(un_texte):
    """fonction permettant de compter le nombre
    de mots présents
    un_texte : type str
    sortie = nombre de mots (int)"""
    un_texte = un_texte.replace('.', ' ')
    liste_du_texte = un_texte.split(' ')
    nouvelle_liste = []
    for mot in liste_du_texte:
        if mot != '' and mot != '\n' :
            nouvelle_liste.append(mot)

    print(nouvelle_liste)
    print(len(nouvelle_liste))

def comptage_mots_differents(un_texte):
    """fonction permettant de compter le nombre
    de mots présents
    un_texte : type str
    sortie = nombre de mots (int)"""
    un_texte = un_texte.replace('.', ' ')
    liste_du_texte = un_texte.split(' ')
    nouvelle_liste = []
    for mot in liste_du_texte:
        if mot != '' and mot != '\n' :
            nouvelle_liste.append(mot)

    print(nouvelle_liste)
    print (len(set(nouvelle_liste)))

def comptage_dico(un_texte):
    """
    Cette fonction compte en utilisant une méthode dictionnaire
    """
    dico_vide = {}
    un_texte = un_texte.replace('.', ' ')
    liste_du_texte = un_texte.split(' ')
    for i in liste_du_texte :
        dico_vide[i] = liste_du_texte.index(i)
    print(dico_vide)
    print("Nombre de mots = {}".format(len(dico_vide.keys())))

def occurrence_mots(un_texte) :
    dico_vide = {}
    un_texte = un_texte.replace('.', ' ')
    liste_du_texte = un_texte.split(' ')
    for i in liste_du_texte :
        if i not in dico_vide :
            dico_vide[i] = 1
        else :
            dico_vide[i] += 1
    print (dico_vide)

texte = """Vous pouvez remplacer ce texte par n\'importe quoi.
Une poésie, un article de journal, des mots aléatoires ou autres.
Vous pouvez aussi ne pas modifier ce texte. L\'important est que la valeur de la variable \'texte\' soit bien une chaîne de caractère.
"""

#comptage(texte)

texte2 = """ Les pigeons se moquent de mon chat """
texte3 = "la la la la"
texte_court = "bonjour ça va va"

#comptage(texte2)
comptage_mots_differents(texte)
comptage_mots_differents(texte2)
comptage_mots_differents(texte3)
comptage(texte3)
comptage_dico(texte3)

occurrence_mots(texte_court)