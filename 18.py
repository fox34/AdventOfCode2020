#!/usr/bin/env python3

import re

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    # Eine Zahl pro Zeile
    input = infile.read().splitlines()

parenthesisRe = re.compile("(\(|\))")
findInnermostParenthesis = re.compile("\(([\d+* ]+)\)")

def resolveBareExpressionLTR(expr):
    if parenthesisRe.search(expr):
        raise Exception("Keine Klammern erlaubt.")
    elements = expr.split(" ")
    result = int(elements[0])
    for i in range(1, len(elements), 2):
        operation = elements[i]
        num = int(elements[i+1])
        if operation == "+":
            result += num
        elif operation == "*":
            result *= num
        else:
            raise Exception("Ungültige Operation: {operation}")
    return result

def resolveParenthesisLTR(expr):
    #print(expr)
    while nextInnerParenthesis := findInnermostParenthesis.search(expr):
        innerExprPosition = (nextInnerParenthesis.start(1), nextInnerParenthesis.end(1))
        innerResult = resolveBareExpressionLTR(nextInnerParenthesis.group(1))
        #print(f"innerGroup = {nextInnerParenthesis.group(1)} = {innerResult}")
        expr = expr[:innerExprPosition[0] - 1] + str(innerResult) + expr[innerExprPosition[1] + 1:]
        #print(f"expr = {expr}")
    return resolveBareExpressionLTR(expr)

sumOfAll = 0
for expr in input:
    result = resolveParenthesisLTR(expr)
    #print(f"{expr} = {result}")
    sumOfAll += result

print(f"Teil 1: Summe aller Einzelstücke: {sumOfAll}")


# Teil 2
sumFinder = re.compile("(\d+) \+ (\d+)")

def resolveBareExpressionSumBeforeMult(expr):
    if parenthesisRe.search(expr):
        raise Exception("Keine Klammern erlaubt.")
    
    while nextSum := sumFinder.search(expr):
        sumPos = (nextSum.start(0), nextSum.end(0))
        if sumPos[0] == 0:
            partBefore = ""
        else:
            partBefore = expr[:sumPos[0]]
        if sumPos[1] == len(expr):
            partAfter = ""
        else:
            partAfter = expr[sumPos[1]:]
        
        innerResult = int(nextSum.group(1)) + int(nextSum.group(2))
        expr = partBefore + str(innerResult) + partAfter
        #print(f"expr = {expr}")
    
    # Wie oben
    elements = expr.split(" ")
    result = int(elements[0])
    for i in range(1, len(elements), 2):
        operation = elements[i]
        num = int(elements[i+1])
        if operation == "+":
            result += num
        elif operation == "*":
            result *= num
        else:
            raise Exception("Ungültige Operation: {operation}")
    return result

# Identisch mit oben, ruft nur andere Funktion auf
def resolveParenthesisSumBeforeMult(expr):
    #print(expr)
    while nextInnerParenthesis := findInnermostParenthesis.search(expr):
        innerExprPosition = (nextInnerParenthesis.start(1), nextInnerParenthesis.end(1))
        innerResult = resolveBareExpressionSumBeforeMult(nextInnerParenthesis.group(1))
        #print(f"innerGroup = {nextInnerParenthesis.group(1)} = {innerResult}")
        expr = expr[0:innerExprPosition[0] - 1] + str(innerResult) + expr[innerExprPosition[1] + 1:]
        #print(f"expr = {expr}")
    return resolveBareExpressionSumBeforeMult(expr)

sumOfAll2 = 0
for expr in input:
    result = resolveParenthesisSumBeforeMult(expr)
    #print(f"{expr} = {result}")
    sumOfAll2 += result

print(f"Teil 2: Summe aller Einzelstücke: {sumOfAll2}")


