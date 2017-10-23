import pandas
import os

'''
Exemple de code qui lit un fichier excel 'info1_pandas_example_input.xlsx'
et fait la moyenne des âges des sujets pour chaque groupe

entrée : fichier excel dans lequel pour un ensemble de sujets appartement à deux groupes différents, 
l'âge de chaque sujet est renseigné (3 colonnes : 'identifiant', 'groupe', 'âge')

sortie : fichier csv ouvrable dans excel et fichier excel correspondant, dans lequel pour
chaque groupe la moyenne des âges des sujets est calculée (colonnes 'groupe' et 'age_moyen')
'''
os.chdir('C:/Users/roca/Documents/AIP2017/examples/data') # à changer en fonction de l'emplacement des fichiers
df = pandas.read_excel('info1_pandas_example_input.xlsx', sep=';')
df.age

df_test1 = df[df.groupe == 'test1']
df_test1.age.sum()
mean_test1 = df_test1.age.mean()

df_test2 = df[df.groupe == 'test2']
mean_test2 = df_test2.age.mean()

# creation du dataframe de sortie:
moyennes = {'groupe': ['test1', 'test2'], 'age_moyen': [mean_test1, mean_test2]}
df_moyennes = pandas.DataFrame.from_dict(moyennes, orient='columns')
df_moyennes.to_csv('info1_pandas_example_output.csv')
df_moyennes.to_excel('info1_pandas_example_output.xlsx', columns=['groupe', 'age_moyen'], index=False)
