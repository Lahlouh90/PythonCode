# La fonction insert prend l'élément à insérer et une séquence triée
# en tant qu'arguments.
# Elle insère l'élement à la place correcte dans la séquence et
#  retourne cette-dernière.

sequence=[2,3,89,1]


def insert(element, sequence):
    if sequence==[]:
        return [element]
    elif element <= sequence[0]:
        return [element] + sequence
    else:
        return[sequence[0]] + insert(element, sequence[1:len(sequence)])


# La fonction merge prend 2 séquences triées comme arguments.
# Elle retourne une fusion des 2 séquences telles que la séquence 
# résultante est triée.

def merge(subSequence1, subSequence2):
    if subSequence1 == []:
        return subSequence2
    elif subSequence2 == []:
        return subSequence1
    else:
        return merge(subSequence1[1:len(subSequence1)], insert(subSequence1[0], subSequence2))




# La fonction mergeSort prend la séquence à trier comme argument. La séquence d'entrée est supposée être une liste.
# Cette fonction retourne une permutation de la séquence d'entrée, triée par ordre croissant.
import math

def mergeSort(sequence):
    n=len(sequence)
    if n== 0 or n == 1:
        return sequence
    else:
        return merge(mergeSort(sequence[0:math.ceil(n/2)]), mergeSort(sequence[math.ceil(n/2):n]))




sequence=[3,89,4,34,100,32,9,231,87,43,430]
f=mergeSort(sequence)
print(f)














