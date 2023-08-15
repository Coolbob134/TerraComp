#Simulator for the Terracomp Project
#GitHub: https://github.com/Coolbob134/TerraComp/ (currently public)

#Takes an output file (Created by the assembler) and runs it as the computer would

import os.path

regA = 0
regB = 0
regC = 0
linecounter = 0

def STA(Value):
    global regA
    regA = int(Value,base = 2)
def STB(Value):
    global regB
    regB = int(Value,base = 2)
def STC(Value):
    global regC
    regC = int(Value,base = 2)
def ADD(Value):
    global regA
    global regB
    global regC
    regC = regA + regB
def DISP(Value):
    print(f"{regC:04b}")
def MOVA(Value):
    global regA
    global regC
    regA = regC
def MOVB(Value):
    global regB
    global regC
    regB = regC

def run_line(inputline):
    global linecounter
    line = inputline.strip()
    cmd = inputline.split(" ")[0]
    if (len(inputline.split(" ")) != 2) & (line != ""):
        raise SyntaxError(f"Incorrect number of arguments at line {linecounter}")
    if (cmd not in commands) & (line != ""):
        raise NameError(f"\"{cmd}\" is not a valid command (line {linecounter})")
    if int(inputline.split(" ")[1],base = 2) > 15:
        raise ValueError(f"Value exceeds maximum of 15 at line {linecounter}")
    commands[cmd](inputline.split(" ")[1])
    

commands = {
    "0001" : STA,
    "0010" : STB,
    "0011" : STC,
    "0100" : ADD,
    "0101" : DISP,
    "0110" : MOVA,
    "0111" : MOVB
}

print("TERRACOMP SIMULATOR\n")
filepath = input("Enter the path of the file to executed:")
if not os.path.exists(filepath):
    raise Exception(f"File \"{filepath}\" does not exist")
print(f"Executing...\n")

with open(filepath) as SourceFile:
    for line in SourceFile:
        linecounter = linecounter + 1
        run_line(line)

print(f"\nDONE!\nLines excecuted:{linecounter}")

