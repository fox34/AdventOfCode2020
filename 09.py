#!/usr/bin/env python3

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = [int(x) for x in infile.read().splitlines()]

# Präambel
rollingWindowLength = 25

for currentIndex in range(rollingWindowLength, len(input)):
    currentNumber = input[currentIndex]
    prevNums = input[currentIndex-rollingWindowLength:currentIndex]
    
    foundSum = False
    for firstSummand in prevNums:
        
        # Aktuelle Zahl > Ziel, Abbruch
        if firstSummand > currentNumber:
            continue
        
        # Suche zweite Zahl
        for secondSummand in prevNums:
            
            # Keine gleichen Zahlen
            if firstSummand == secondSummand:
                continue
            
            # Summe gefunden
            if firstSummand + secondSummand == currentNumber:
                foundSum = True
                break # secondSummand
        
        # Summe gefunden, Schleife stoppen
        if foundSum:
            break # firstSummand
    
    
    if not foundSum:
        
        # Teil 1: 373803594
        print(f"Keine Summanden für {currentNumber} gefunden")
        
        # Teil 2: 51152360
        summands = []
        startingIndex = 0
        currentIndex = 0
        while True:
            
            # Match
            if sum(summands) == currentNumber:
                minSummand = min(summands)
                maxSummand = max(summands)
                sumOfBoth = minSummand + maxSummand
                print(f"Summanden gefunden, kleinster: {minSummand}, größter: {maxSummand}, Summe: {sumOfBoth}")
                break # while
            
            # Reset
            if sum(summands) > currentNumber:
                summands = []
                startingIndex += 1
                currentIndex = startingIndex
            
            # Aktuelle Zahl ignorieren
            if input[currentIndex] == currentNumber:
                currentIndex += 1
            
            summands.append(input[currentIndex])
            currentIndex += 1
        
        # Danach stoppen
        break # for...in range

            