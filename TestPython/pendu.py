

import os

from donnee import *

from fonction import *

with open('Score.txt', 'r') as file:
    Mes_Score = json.load(file)


# "Tomates 7", "Pommes 6", "Grenade 7", "Patate 6"



def pendu():
    nom=input("Veuillez taper votre nom svp ")
    nom=nom
    Enregistrement(nom)
    Nb=Recherche(LeMot, NbC)
    print("ya Sa7bi", nom," tu as donc ", Nb, "points, mabrouk 7bibi")
    with open('Score.txt', 'r') as file:
        Mes_Score = json.load(file)
    Mes_Score[nom] = Mes_Score[nom]+ Nb
# Enregistrer le dictionnaire dans un fichier :
    with open('Score.txt', 'w') as file:
       json.dump(Mes_Score, file)


pendu()


