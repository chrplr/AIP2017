#! /usr/bin/env python

""" 
Un magasin propose des CD à 15€ et des des DVD à 20€.

Pour tout achat d'au moins 4 CD,  il est consenti une réduction de 20% sur les CD.

Pour l'achat d'au moins 3DVD, il est consenti une réduction de 15% sur le DVD.

Construire un programme permettant d'obtenir le prix à payer suivant le nombre n de CD et m de DVD achetés
"""

PRIX_CD = 15  # en €
PRIX_DVD = 20  # en €


SEUIL_CD = 4
RABAIT_CD = 20  # en %
SEUIL_DVD = 3
RABAIT_DVD = 15  # en %

PRIX_CD_SOLDE = PRIX_CD * ((100 - RABAIT_CD)/100)
PRIX_DVD_SOLDE = PRIX_DVD * ((100 - RABAIT_DVD)/100)

def prix(n_cd=0, n_dvd=0):
    """ Calcule le prix total en fonction du nombre de CD et de DVD """
    if n_cd < SEUIL_CD:
        prix_cd = n_cd * PRIX_CD
    else:
        prix_cd = n_cd * PRIX_CD_SOLDE
    if n_dvd < SEUIL_DVD:
        prix_dvd = n_dvd * PRIX_DVD
    else:
        prix_dvd = n_dvd * PRIX_DVD_SOLDE
    return prix_cd + prix_dvd   # prix total


if __name__ == '__main__':
    print(prix(1, 1))
    print(prix(2, 2))
    print(prix(3, 1))
    print(prix(4, 1))
    print(prix(4, 2))
    print(prix(4, 3))
    print(prix(4, 4))
    print(prix(n_cd=5))
    print(prix(n_dvd=5))

    for i in range(10):
        for j in range(10):
            print("cd={} dvd={} -> prix={}€".format(i, j, prix(i, j)))
