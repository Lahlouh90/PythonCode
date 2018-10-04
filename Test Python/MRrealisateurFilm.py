
# Fonctionnalité de MapReduce, permetant de joindre dans une big data base
# les films aux nom des realistaure

# comme ici, on a diviser notre big data base en plusier partit
# affin d'établir la parralelisation, le key, va representer le nom du fichier
# ou sont tirer nos données

def map(key, value):
    intermediate = []
    for i in value:
        intermediate.append((i[1], (i[0],i[1:]))) # i[1] est ici la nouvelle clée representant
    return intermediate                           # le id des realicatuers
                                                  # (i[@], i[1,:]) est le tuplet representant le nom de la table + nom du film ou du realisateur


