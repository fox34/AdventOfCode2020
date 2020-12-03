#!/usr/bin/env python3

# Eingabe lesen
with open("input/01.txt") as infile:
    input = infile.read().split("\n")

# Teil 1
found = False
solution = False
i = 0
for num in input:
    i += 1
    for num2 in input[i:]:
        if int(num) + int(num2) == 2020:
            solution = int(num) * int(num2)
            print(f"Gefunden: {num} + {num2} = 2020, {num} * {num2} = {solution}")
            break
    
    if solution != False:
        break


# Teil 2
found = False
solution = False
i1 = 0
i2 = 0
for num in input:
    i1 += 1
    for num2 in input[i1:]:
        i2 = i1 + 1
        for num3 in input[i2:]:
            if int(num) + int(num2) + int(num3) == 2020:
                solution = int(num) * int(num2) * int(num3)
                print(f"Gefunden: {num} + {num2} + {num3} = 2020, {num} * {num2} * {num3} = {solution}")
                break
        
        if solution != False:
            break
    if solution != False:
        break


