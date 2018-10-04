
# Mthode des conteneure


class ZDict:
    def __init__(self):
        self._dictionnaire={}
    def __getitem__(self, index):
        return self._dictionnaire[index]
    def __setitem__(self, index, valeur):
        self._dictionnaire[index]=valeur

# les Appels
montr=ZDict()

montr._dictionnaire["beuf"]="oeuf"

print(montr._dictionnaire["beuf"])

"""



######  Etudes de la methode contains
"""
# classe liste

class List:

    def __init__(self, nombre):
        self.nombre=nombre
        self.ma_liste= [1,2,3,4,5]

    def __contains__(self, nombre):
        print("voysons voir si le nombre : {}, est dans la liste".format(self.nombre))
        return self.ma_liste.__contains__(nombre)



Eub=List(8)

print(Eub.__contains__(8))



"""
######  Etudes de la methode Len


class List:

    def __init__(self):

        self.ma_liste= [1,2,3,4,5]

    def __len__(self):
        print("voysons voir la taille de la liste : {}".format(self.ma_liste))
        return self.ma_liste.__len__()



Eub=List()

print(Eub.__len__())
"""


########  Etute de la methode __add__

"""
class Duree:
    def __init__(self, min=0, sec=0):
        self.min=min
        self.sec=sec
    def __str__(self):
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        nouvelle_duree=Duree()
        nouvelle_duree.min=self.min
        nouvelle_duree.sec=self.sec

        nouvelle_duree.sec += objet_a_ajouter

        if nouvelle_duree.sec >=60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        return nouvelle_duree


Eub=Duree(10,30)
print(Eub)

print(Eub+65)

"""




########  Etute de la methode __radd

"""
class Duree:
    def __init__(self, min=0, sec=0):
        self.min=min
        self.sec=sec
    def __str__(self):
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        nouvelle_duree=Duree()
        nouvelle_duree.min=self.min
        nouvelle_duree.sec=self.sec

        nouvelle_duree.sec += objet_a_ajouter

        if nouvelle_duree.sec >=60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        return nouvelle_duree

    def __radd__(self, objet_a_ajouter):
        return self + objet_a_ajouter


Eub=Duree(10,30)
print(Eub)

print(65+Eub)

"""


### Etude de comparaison

"""
class Duree:
    def __init__(self, min1=0, sec1=0):
        self.min1=min1
        self.sec1=sec1
        self.min=5
        self.sec=30

    def __str__(self):
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __eq__(self, min1,sec1):
        #Test si self et autre_duree sont �gales
        return self.sec== self.sec1 and self.min==self.min1

    def __gt__(self, min1, sec1):
        #Test si self > autre_duree
        # On calcule le nombre de secondes de self et l autre mesure de compar
        nb_sec = self.sec + self.min * 60
        nb_sec1= self.sec1 + self.min1 * 60
        return nb_sec > nb_sec1




Eub=Duree(3,30)
print(Eub.__eq__(3,30))
print(Eub.__gt__(3,30))


"""

# Etude de __getstate__

""""
class Temp:

    def __init__(self):
        #onstructeur de notre objet
        self.attrinut_1="une valeur"
        self.attrinut_2="une autre valeur"
        self.attribut_temporaire =5

    def __getstate__(self):
        #renvoie le dictionnaire d'attributs � serialiser
        dict_attr=dict(self.__dict__)
        dict_attr["attrinut_temporaire"]=0
        return dict_attr

Eub=Temp()

"""