#!/usr/bin/env python3

import math # math.floor

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().splitlines()

class seatFinder:
    def __init__(self, seatDefinition):
        self.rowSteps = seatDefinition[0:7]
        self.columnSteps = seatDefinition[7:]

    def getRow(self):
        currentRange = [0, 127]
        for step in self.rowSteps:
            if step == "F":
                currentRange[1] = math.floor(sum(currentRange) / 2)
            elif step == "B":
                currentRange[0] = math.ceil(sum(currentRange) / 2)
            else:
                raise Exception(f"Ungültige Reihendefinition: {step}")
        return currentRange[0]
    
    def getCol(self):
        currentRange = [0, 7]
        for step in self.columnSteps:
            if step == "L":
                currentRange[1] = math.floor(sum(currentRange) / 2)
            elif step == "R":
                currentRange[0] = math.ceil(sum(currentRange) / 2)
            else:
                raise Exception(f"Ungültige Spaltendefinition: {step}")
        return currentRange[0]
    
    def getSeatId(self):
        return self.getRow() * 8 + self.getCol()


# Teil 1
seatIdList = [] # Für Teil 2 Liste ohnehin nötig, sonst würde ein max() in der Schleife reichen
for seatDefinition in input:
    currentSeatFinder = seatFinder(seatDefinition)
    seatIdList.append(currentSeatFinder.getSeatId())
maxSeatId = max(seatIdList)

print(f"Höchste Sitzplatz-ID: {maxSeatId}")


# Teil 2
def findMySeat(seatIdList):
    for currentRow in range(0, 127):
        for currentCol in range(0, 7):
            currentSeatId = currentRow * 8 + currentCol
            if currentSeatId in seatIdList:
                continue
            if currentSeatId - 1 in seatIdList and currentSeatId +1 in seatIdList:
                print(f"Eigene Sitzplatz-ID: {currentSeatId}")
                
                # Nach gefundenem Sitzplatz weitere Suche stoppen
                return

findMySeat(seatIdList)
