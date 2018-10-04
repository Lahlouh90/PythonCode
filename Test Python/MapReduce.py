# fonction de base
from collections import defaultdict

def wordCount(text):
    counts=defaultdict(int)
    for word in text.split():
        counts[word.lower()] +=1
    return counts

# logique Map reduce, divisier pour mieux regner

D1 = {"./lot1.txt" : "jour lève notre grisaille"}
D2 = {"./lot2.txt" : "trottoir notre ruelle notre tour"}
D3 = {"./lot3.txt" : "jour lève notre envie vous"}
D4 = {"./lot4.txt" : "faire comprendre tous notre tour"}

# fonction map
def map(key, value):
    intermediate=[]
    for word in value.split():
        intermediate.append((word,1))
    return print(intermediate)

map("./lot1.txt","jour lève notre grisaille" )

# fonctionc reduce
def reduce(key, values):
    resuly = 0
    for c in values:
        result = result + c
    return(key, result)
