#!/usr/bin/env python3

# Eingabe lesen
with open("input/02.txt") as infile:
    input = infile.read().split("\n")


# Passwort überprüfen
def password_is_valid_old_rules(dataset):
    # Regel einlesen
    rule, password = dataset.split(": ", 1)
    limits, ruleLetter = rule.split(" ", 1)
    lowerLimit, upperLimit = [int(num) for num in limits.split("-", 1)]
    
    # Variablen:
    # - password: string
    # - ruleLetter: string
    # - lowerLimit, upperLimit: int
    
    # Anzahl Buchstaben zwischen beiden Limits
    return lowerLimit <= password.count(ruleLetter) <= upperLimit


# Teil 1: Anzahl korrekter Passwörter
numCorrect = 0
for password in input:
    if password_is_valid_old_rules(password):
        numCorrect += 1

# 383
print(f"Anzahl korrekter Passwörter nach alten Regeln: {numCorrect}")



# Teil 2: Korrekte "Firmenphilosophie"

# Passwort überprüfen
def password_is_valid_new_rules(dataset):
    # Regel einlesen
    rule, password = dataset.split(": ", 1)
    positions, ruleLetter = rule.split(" ", 1)
    firstPos, secondPos = [int(num) for num in positions.split("-", 1)]
    
    return (password[firstPos - 1] == ruleLetter) ^ (password[secondPos - 1] == ruleLetter)
    

# Teil 2: Anzahl korrekter Passwörter nach neuen Regeln
numCorrect = 0
for password in input:
    if password_is_valid_new_rules(password):
        numCorrect += 1

# 272
print(f"Anzahl korrekter Passwörter nach neuen Regeln: {numCorrect}")

