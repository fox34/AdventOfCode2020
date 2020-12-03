#!/usr/bin/env python3

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().splitlines()

# Bäume auf vorgegebenem Weg zählen
def treeEncounters(treeMap, xStep, yStep):
    numTrees = 0
    xPos = 0
    for yPos in range(0, len(treeMap), yStep):
        line = treeMap[yPos]
        if line[xPos % len(line)] == "#":
            numTrees += 1
        xPos += xStep
    
    return numTrees


# Teil 1: Anzahl Bäume für xstep = 3, ystep = 1
# 225
numTrees = treeEncounters(input, 3, 1)
print(f"Teil 1: Anzahl Bäume getroffen: {numTrees}")


# Teil 2: Multiplikation aller getroffenen Bäume für alle Varianten
variations = [(1,1), (3,1), (5,1), (7,1), (1,2)]
multipliedNumberOfTrees = 1
for variation in variations:
    multipliedNumberOfTrees *= treeEncounters(input, variation[0], variation[1])

# 1115775000
print(f"Teil 2: Produkt der gesamt angetroffenen Bäume für alle Varianten: {multipliedNumberOfTrees}")
