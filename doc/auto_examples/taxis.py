#! /usr/bin/env python

""" 
Deux compagnies de taxis proposent des tarifs différents:

* Tarif A: prise en charge de 4.80€ puis 1.15€ par km parcouru
* Tarif B: prise en charge de 3.20€ puis 1.20€ par km parcouru

Ecrire un programme permettant de décider quelle compagnie choisir en fonction du nombre de kms à parcourir.
"""

def tarif_A(distance):
    return 4.80 + (1.15 * distance)  

def tarif_B(distance):
    return 3.20 + (1.20 * distance)  

# affichage 
for d in range(100):
    print("{} -> tarifA = {}; tarifB = {}".format(d, tarif_A(d), tarif_B(d)))

def choix(distance):
    a = tarif_A(distance)
    b = tarif_B(distance)
    if a < b:
        return ("A", a)
    else:
        return ("B", b)


print(10, choix(10))
print(40, choix(40))
print(100, choix(100))
