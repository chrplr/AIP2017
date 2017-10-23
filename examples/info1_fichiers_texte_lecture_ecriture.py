import os

directory = os.path.join("C:/Users", "roca", "Documents", "cogmaster2017_info1",
"session4")
os.chdir(directory)

# Creation d'un fichier dans Atom. avec mon_texte.txt
# avec bonjour ! dedans.

## Lecture avec open/close
mon_fichier = open('mon_fichier.txt', 'r')
contenu = mon_fichier.read()
mon_fichier.close()

## Ouverture en mode écriture:
mon_fichier = open('mon_fichier.txt', 'w')
mon_fichier.write('ça va?') # on regarde le fichier.
#si on ne ferme pas on n'enregistre pas :
mon_fichier.close()
# qu'est-ce qu'il s'est passé ? : 'Bonjour!' a été effacé.
# pb d'encodage : Edit>Select Encoding: utf-8

## Ouverture en mode écriture en changeant l'encodage
mon_fichier = open('mon_fichier.txt', 'w', encoding='utf-8')
mon_fichier.write('ça va?')
mon_fichier.close() # verif: OK!!

## Ouverture en mode append:
mon_fichier = open('mon_fichier.txt', 'a', encoding='utf-8')
mon_fichier.write('Et toi ?')
mon_fichier.close()

## Ouverture avec with
with open('mon_fichier.txt', 'a', encoding='utf-8') as fichier:
    fichier.write('\n Je viens bien merci.')

## avec print:
print('J\'adore les cours python !',
      file=open('mon_fichier.txt', 'a', encoding='utf-8'))

# Mise en application avec un dictionnaire:
'''
Enregistrer un dictionnaire et enregistrer le.
'''
mon_dico = {"chemises":"10", "pantalons": "4"}

#USING open et close
out_file = open('donnees_1.txt', 'w')
out_file.write(str(mon_dico))
out_file.close() #si on ne ferme pas on n'enregistre pas

#Avec with:
with open('donnees_2.txt', 'w') as fichier:
    fichier.write(str(mon_dico))

#using print
print(mon_dico, file=open('donnees_3.txt', 'w', encoding='utf-8'))

#avec csv.
print('robes', 5, sep = ';', file=open('donnees_4.txt', 'w', encoding='utf-8'))

for cle, valeur in mon_dico.items():
    print(cle, valeur, sep=';', file=open('donnees_4.txt', 'w', encoding='utf-8'))

#avec csv sans ecraser le fichier:
for cle, valeur in mon_dico.items():
    print(cle, valeur, sep=';', file=open('donnees_5.txt', 'a', encoding='utf-8'))

#USING PANDAS:
import pandas
data_frame = pandas.DataFrame.from_dict(mon_dico, orient='index')
#pandas.DataFrame.from_dict?
data_frame.to_csv('data.csv', header=False)

#PICKLE
import pickle
with open('donnees.txt', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(mon_dico)
