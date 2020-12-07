#!/usr/bin/env python3

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().splitlines()

class BagParser:
    
    def __init__(self, bagDefinition):
        bagName, contents = bagDefinition.split(" contain ", 1)
        
        # Singular
        self.bag = bagName[:-1]
        
        # Inhalte
        self.contents = {}
        if contents != "no other bags.":
            contents = contents[:-1].split(", ")
            for content in contents:
                num, name = content.split(" ", 1)
                num = int(num)
                if (num > 1):
                    name = name[:-1]
                    
                self.contents[name] = num
    
    def resolveRecursiveContents(self, contents, allOtherBags):
        resolvedContents = contents.copy()
        for name, amount in contents.items():
            parser = allOtherBags[name]
            otherContents = parser.resolveRecursiveContents(parser.contents, allOtherBags)
            for name2, amount2 in otherContents.items():
                if name2 in resolvedContents:
                    resolvedContents[name2] += amount * amount2
                else:
                    resolvedContents[name2] = amount * amount2
        
        return resolvedContents
    
    def canContainShinyGoldBag(self):
        pass

# Einlesen
bagProperties = {}
for bag in input:
    parser = BagParser(bag)
    bagProperties[parser.bag] = parser

for bag, parser in bagProperties.items():
    parser.resolvedContents = parser.resolveRecursiveContents(parser.contents, bagProperties)

# Teil 1
howManyCanHoldAShinyGoldBag = 0
for bag, parser in bagProperties.items():
    if "shiny gold bag" in parser.resolvedContents:
        howManyCanHoldAShinyGoldBag += 1

# 144
print(f"Teil 1: {howManyCanHoldAShinyGoldBag} Farben können einen gold-glitzernden Koffer beinhalten.")

# Teil 2
howManyBagsAreInMyShinyGoldBag = sum(bagProperties["shiny gold bag"].resolvedContents.values())
print(f"Teil 1: {howManyBagsAreInMyShinyGoldBag} Koffer sind in meinem gold-glitzernden Koffer enthalten.")
