#!/usr/bin/env python3

import math # math.floor

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().split("\n\n")

class groupAnswerParser:
    def __init__(self, groupDefinition):
        self.people = groupDefinition.splitlines()
    
    def parseAllAnswers(self):
        allAnswers = []
        for person in self.people:
            for answer in person:
                if not answer in allAnswers:
                    allAnswers.append(answer)
        
        return len(allAnswers)
    
    def parseAnswersThatEveryoneAnswered(self):
        allAnswers = {}
        for person in self.people:
            for answer in person:
                if not answer in allAnswers:
                    allAnswers[answer] = 1
                else:
                    allAnswers[answer] += 1
        
        numAnswersThatEveryoneAnswered = 0
        for answer, occurences in allAnswers.items():
            if occurences == len(self.people):
                numAnswersThatEveryoneAnswered += 1
        
        return numAnswersThatEveryoneAnswered

# Teil 1
numAnswers = 0
numAllAnswers = 0
for groupDefinition in input:
    answerParser = groupAnswerParser(groupDefinition)
    numAnswers += answerParser.parseAllAnswers()
    numAllAnswers += answerParser.parseAnswersThatEveryoneAnswered()

# 6625
print(f"Teil 1: Anzahl beantworteter Fragen: {numAnswers}")

# 3360
print(f"Teil 2: Anzahl Fragen, die alle beantwortet haben: {numAllAnswers}")

