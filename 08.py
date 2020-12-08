#!/usr/bin/env python3

# Eingabe lesen
today = __file__.rsplit("/", 1)[-1].removesuffix(".py")
with open(f"input/{today}.txt") as infile:
    input = infile.read().splitlines()

class InfiniteLoopException(Exception):
    pass

class OutOfBoundsException(Exception):
    pass

class CodeParser:
    def __init__(self, instructions):
        self.instructions = instructions
        self.instructionPointer = 0
        self.accumulator = 0
        self.validOperations = ("nop", "acc", "jmp")
    
    def run(self):
        
        executedLines = []
        while True:
            
            # Out of bounds
            if self.instructionPointer >= len(self.instructions):
                raise OutOfBoundsException(f"Out of bounds. Stopping.")
                return
            
            # Loop
            if self.instructionPointer in executedLines:
                raise InfiniteLoopException(f"Infinite loop. Stopping.")
                return
            
            executedLines.append(self.instructionPointer)
            
            # Befehl parsen
            instruction = self.instructions[self.instructionPointer]
            operation, parameter = instruction.split(" ", 1)
            if operation not in self.validOperations:
                raise Exception(f"Ungültige Operation: {operation}")
            
            # Befehl aufrufen
            getattr(self, operation)(parameter)
    
    
    def tryFixInfiniteLoop(self):
        lineCounter = 0
        
        # Alle Befehle einzeln prüfen und bei jmp und nop Tausch versuchen
        while lineCounter < len(self.instructions):
            
            operation, parameter = self.instructions[lineCounter].split(" ", 1)
            
            # acc nicht tauschen
            if operation == "acc":
                lineCounter += 1
                continue
            
            # Tausch nötig
            currentInstructionSet = self.instructions[:]
            
            # Befehl tauschen
            if operation == "nop":
                currentInstructionSet[lineCounter] = f"jmp {parameter}"
            elif operation == "jmp":
                currentInstructionSet[lineCounter] = f"nop {parameter}"
            else:
                raise Exception(f"Ungültiger Befehl: {operation}")
            
            # Mit getauschten Werten starten
            parser = CodeParser(currentInstructionSet)
            try:
                parser.run()
            
            # Offenbar nicht erfolgreich
            except InfiniteLoopException:
                lineCounter += 1
            
            # Erfolgreich
            except OutOfBoundsException:
                return parser
    
    
    def nop(self, param):
        self.instructionPointer += 1
    
    def acc(self, param):
        self.accumulator += int(param)
        self.instructionPointer += 1
    
    def jmp(self, param):
        self.instructionPointer += int(param)

# Teil 1: 1939
parser = CodeParser(input)
try:
    parser.run()
except InfiniteLoopException as e:
    print(f"Teil 1: Accumulator vor infinite loop: {parser.accumulator}")
else:
    print(f"Teil 1: Fehler: Kein loop erkannt")


# Teil 2: 2212
parser = parser.tryFixInfiniteLoop()
print(f"Teil 2: Accumulator vor oob: {parser.accumulator}")
