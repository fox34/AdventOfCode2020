#!/usr/bin/env python3

input = [int(x) for x in "0,1,5,10,3,12,19".split(",")]

# zahl = (letztes, vorletztes)
memory = {}

# Initialwerte speichern
i = 1
for num in input:
    memory[num] = [i]
    lastNumber = num
    i += 1

#print(memory)

# Teil 1: 2020
#numRounds = 2020
# Teil 2: 30000000
numRounds = 30000000
# i *nicht* zurücksetzen
while i <= numRounds:
    
    if i % 1000000 == 0:
        print(f"Runde {i}")
    
    # Wurde in der letzten Runde das erste Mal genannt
    if len(memory[lastNumber]) == 1:
        #print(f"{lastNumber} wurde das erste mal genannt. Neue Zahl = 0")
        lastNumber = 0
        
    else:
        # Wurde bereits gesagt
        #print(f"{lastNumber} wurde bereits genannt: {memory[lastNumber]}")
        lastNumber = memory[lastNumber][0] - memory[lastNumber][1]
    
    # Nummer merken
    if lastNumber in memory.keys():
        memory[lastNumber] = [i, memory[lastNumber][0]]
    else:
        memory[lastNumber] = [i]
    
    i += 1

# Teil 1: 1373
# Teil 2: 112458
print(f"Nummer an der Stelle {numRounds}: {lastNumber}")
