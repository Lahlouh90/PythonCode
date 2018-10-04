
# Etude sort, sorted
"""
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort()

print(prenoms)

prenom = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]

print(sorted(prenom))
print(prenom)

print(sorted([1, 8, -2, 15, 9]))

print(sorted(["1", "8", "-2", "15", "9"]))

print(sorted([1, "8", "-2", "15", 9]))
"""

# utilisation des Key
"""
etudiants=[
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15)
          ]

print(sorted(etudiants)) # va trier automatiquement selon la premiere colone

# si on veut triser en fonction des notes, nous devons utiliser la fonction lambda


print(sorted(etudiants, key= lambda colonnes : colonnes[2]))

"""

# Trie dans une classe

""" 
class Etudiant:
    #Classe représentant un étudiant.

    #On représente un étudiant par son prénom (attribut prenom), son âge
    #(attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    #Paramètres du constructeur :
     #   prenom -- le prénom de l'étudiant
     #   age -- l'âge de l'étudiant
      #  moyenne -- la moyenne de l'étudiant

    

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Etudiant {} (age = {}, moyenne={}>".format(self.prenom, self.age, self.moyenne)


etudiants=[
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

print(etudiants)

# trie en fonction de la moyenne
print(sorted(etudiants, key = lambda etudiant: etudiant.moyenne ))

# trie inverse en fonction de l age

print(sorted(etudiants, key = lambda etudiant: etudiant.age, reverse=True ))

"""

# Tri avec le modure operateur
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

from operator import itemgetter

print(sorted(etudiants, key=itemgetter(2)))


class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

from operator import attrgetter

print(sorted(etudiants, key=attrgetter("age", "moyenne")))


class LigneInventaire:

    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{})>".format(
                self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

print(sorted(inventaire, key= attrgetter("prix","quantite")))