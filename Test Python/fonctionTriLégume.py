
# cette fonction va trier par ordre decroissant la list inventaire

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
 ]

Inv=[ (nb, non) for(non, nb) in inventaire]
InvR=sorted(Inv, reverse=True)
InvRR=[ (nom, nb) for (nb, nom) in InvR]
print(InvRR)

