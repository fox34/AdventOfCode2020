#!/usr/bin/env python3

import re # re.split

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().split("\n\n")


class PassportValidator:
    
    def __init__(self):
        self.requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.optionalFields = ['cid']
    
    # Passport einlesen
    def parse_passport(self, passport):
        passportDataRaw = re.split(" |\n", passport)
        passportData = {}
        for dataset in passportDataRaw:
            var, value = dataset.split(":")
            passportData[var] = value
        return passportData
    
    
    # Alle notwendigen Felder enthalten
    def passport_contains_required_fields(self, passport):
        passportData = self.parse_passport(passport)
        for requiredField in self.requiredFields:
            if requiredField not in passportData:
                return False
        
        return True
    
    
    # Alle notwendigen Felder enthalten und Daten sind gültig
    def passport_is_valid(self, passport):
        if not self.passport_contains_required_fields(passport):
            return False
        
        passportData = self.parse_passport(passport)
        for key, value in passportData.items():
            if not self.field_is_valid(key, value):
                return False
        
        return True
    
    # Prüfe angegebenes Feld auf Gültigkeit
    def field_is_valid(self, field, value):
        return {
            "byr": self.validate_byr,
            "iyr": self.validate_iyr,
            "eyr": self.validate_eyr,
            "hgt": self.validate_hgt,
            "hcl": self.validate_hcl,
            "ecl": self.validate_ecl,
            "pid": self.validate_pid,
            "cid": self.validate_cid
        }.get(field, lambda: "Ungültiges Feld!")(value)
    
    def validate_byr(self, value):
        try:
            return len(value) == 4 and 1920 <= int(value) <= 2002
        except:
            return False
    
    def validate_iyr(self, value):
        try:
            return len(value) == 4 and 2010 <= int(value) <= 2020
        except:
            return False
    
    def validate_eyr(self, value):
        try:
            return len(value) == 4 and 2020 <= int(value) <= 2030
        except:
            return False
    
    def validate_hgt(self, value):
        if value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        else:
            return False
    
    def validate_hcl(self, value):
        return re.match("#[a-h0-9]{6}$", value)
    
    def validate_ecl(self, value):
        return value in "amb blu brn gry grn hzl oth".split(" ")
    
    def validate_pid(self, value):
        return re.match("\d{9}$", value)
    
    def validate_cid(self, value):
        return True


# Teil 1
validator = PassportValidator()
numValidPassports = 0
for passport in input:
    if validator.passport_contains_required_fields(passport):
        numValidPassports += 1

print(f"Anzahl Reisepässe mit allen Daten exkl. cid: {numValidPassports}")


# Teil 2
numValidPassports = 0
for passport in input:
    if validator.passport_is_valid(passport):
        numValidPassports += 1

print(f"Anzahl Reisepässe mit gültigen Daten exkl. cid: {numValidPassports}")


