
# -*-coding:Latin-1 -*

import os
# Programme testant si une ann�e, saisie par l'utilisateur, est bissextile ou non

"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'� max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

os.system("pause")