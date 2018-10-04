
# -*-coding:Latin-1 -*

import os

from donnee import *

import json

import random

with open('Score.txt', 'r') as file:
    Mes_Score = json.load(file)


nom='Aziz'

def Enregistrement(nom):

    # cette fonction permet à l'utilisateur de se faire connaitre par le systeme en entrant son prénom
    # le systeme lui envera sont score actuelle
    # si l'utilisateur est nouveax, la fonction l'ajoutera dans le dictionnaire et lui donnera pour score 0
    global Mes_Score
    print("Bonjour",nom)
    if nom in Mes_Score:
        return print("votre score est actuellement de de:",Mes_Score[nom])
    else:
        print("c'est votre premiere parti, votre score est donc de 0")
        Mes_Score[nom]=0
        # Enregistrer le dictionnaire dans un fichier :
        with open('Score.txt', 'w') as file:
            json.dump(Mes_Score, file)


#Enregistrement(nom='Khanez')






# "Tomates 7", "Pommes 6", "Grenade 7", "Patate 6"

N = len(Mots)
LeMot = Mots[random.randrange(0,N-1)]

liste = [elt for elt in LeMot] # nous permet de sperarer lettre par lettre le mot choisis


def Recherche(LeMot,NbC):
    global Nb
    Nb=NbC
    global affichage
    Mem=[]
    for y, param in enumerate(LeMot):
         Mem.append('_')
    print("Le mots recherché est de cette forme ", Mem, "soit ",len(LeMot),"lettres"," Bon courage ya Sa7bi :-)")
    stop=0
    while (Nb > 0 | stop<len(LeMot)) :
       print("Vous avez", Nb,"chance de trouver le mot, veuillez choisir une lettre")
       LE=input()
       Affichage = []
       # construction de la variable mémoire
       while len(LE) != 1:
            print("vous avez tappé plus lettre veillez saisir une lettre")
            LE=input()
       LeMot = LeMot.lower()
       LE = LE.lower()
       a=[]
       for i, elt in enumerate(LeMot):
            if LE == elt:
               Affichage.append(LeMot[i])
               a.append(1)
            else:
               Affichage.append('_')
               a.append(0)

       for j, val in enumerate(Affichage):
            if Mem[j] == '_':
               Mem[j] = val
            else:
                Mem[j] = Mem[j]
       if sum(a)==0:
           Nb = Nb - 1
           stop=stop
       else:
           Nb=Nb
           stop=stop+sum(a)
       print(" ".join(Mem))
    print("vous avez gagné", Nb,"points")
    return Nb

#Recherche(LeMot,NbC)


