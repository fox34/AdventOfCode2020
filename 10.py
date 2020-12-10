#!/usr/bin/env python3

# Zeitmessung
# from time import perf_counter
# class Timer:
#     def tic(self, operation):
#         print(f"\033[38;5;237m{operation}... ", end="")
#         self.tic_time = perf_counter()
#     def toc(self):
#         duration = round(perf_counter() - self.tic_time, 4)
#         print(f"{duration}ms.\033[0m")
# perf = Timer()

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    # Eine Zahl pro Zeile
    input = [int(x) for x in infile.read().splitlines()]

input = [int(x) for x in """16
10
15
5
1
11
7
19
6
12
4""".splitlines()]

# Sortieren
input.sort()

# Eingang = Maximaler Adapterwert + 3
requiredInputJoltage = max(input) + 3
sourceJoltage = 0
print(f"Benötigte Spannung: {requiredInputJoltage} jolts.")

# Teil 1
stepCounter = {1: 0, 2: 0, 3: 0}
prevJoltage = sourceJoltage
for outJoltage in input + [requiredInputJoltage]:
    stepCounter[outJoltage - prevJoltage] += 1
    prevJoltage = outJoltage

print(f"Anzahl Schritte: 1: {stepCounter[1]}, 2: {stepCounter[2]}, 3: {stepCounter[3]}")
# 1984
print(f"Teil 1: Anzahl 1er-Schritte * Anzahl 3er-Schritte = {stepCounter[1] * stepCounter[3]}")


# Teil 2: Rekursiv = no good.
# class PermutationFinder:
#     def __init__(self, steps, sourceJoltage, requiredInputJoltage):
#         self.steps = steps
#         self.sourceJoltage = sourceJoltage
#         self.requiredInputJoltage = requiredInputJoltage
#         self.numPaths = 0
#         #self.paths = []
#     
#     def doFind(self):
#         self.iterate([self.sourceJoltage])
#     
#     def iterate(self, currentPath):
#         currentJoltage = currentPath[-1]
#         
#         # Ende
#         if currentJoltage == self.requiredInputJoltage - 3:
#             #self.paths.append(currentPath)
#             self.numPaths += 1
#             
#             if self.numPaths % 1000000 == 0:
#                 print(f"Gefundene Pfade: {self.numPaths}...")
#             
#             return
#         
#         for i in range(1,4):
#             if currentJoltage + i in self.steps:
#                 self.iterate(currentPath + [currentJoltage + i])
# 
# 
# permutationFinder = PermutationFinder(input, sourceJoltage, requiredInputJoltage)
# permutationFinder.doFind()
# print(f"Teil 2: Anzahl Permutationen: {permutationFinder.numPaths}")



