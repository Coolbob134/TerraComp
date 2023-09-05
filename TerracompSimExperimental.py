#Simulator for the Terracomp project
#GitHub: https://github.com/Coolbob134/TerraComp/ (currently public)

#Takes an output file (Created by the assembler) and runs it as the computer would
#Experimental version (Has Jump, Return and is 8 bit)

import os.path

memsize = 0 #Size of memory
regA = 0    #Register A
regB = 0    #Register B
regC = 0    #Register C
regP = 0    #Jump register for return function
memcounter = 0 #Pointer for address in memory
finished = False    #To check if all code has been executed
memory = []         #Simulates the computer's memory

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
def JMP(Value):
    global regP
    global memcounter
    regP = memcounter
    memcounter = int(Value,base = 2) - 1
def RET(Value):
    global regP
    global memcounter
    memcounter = regP
def HALT(Value):
    global finished
    finished = True
def run_line(inputline):
    global memcounter
    line = inputline.strip()
    cmd = inputline.split(" ")[0]
    if (len(inputline.split(" ")) != 2) & (line != ""):
        raise SyntaxError(f"Incorrect number of arguments at line {memcounter}")
    if (cmd not in commands) & (line != ""):
        raise NameError(f"\"{cmd}\" is not a valid command (line {memcounter})")
    if int(inputline.split(" ")[1],base = 2) > 255:
        raise ValueError(f"Value exceeds maximum of 15 at line {memcounter}")
    commands[cmd](inputline.split(" ")[1])

commands = {
    "0001" : STA,
    "0010" : STB,
    "0011" : STC,
    "0100" : ADD,
    "0101" : DISP,
    "0110" : MOVA,
    "0111" : MOVB,
    "1000" : JMP,
    "1001" : RET,
    "1111" : HALT
}

print("TERRACOMP SIMULATOR\n")
filepath = input("Enter the path of the file to executed:")
if not os.path.exists(filepath):
    raise Exception(f"File \"{filepath}\" does not exist")
print(f"Executing...\n")

with open(filepath) as SourceFile:
    for line in SourceFile:
        memsize = memsize + 1
        memory.append(line)


while memcounter <= memsize and finished == False:
    run_line(memory[memcounter])
    memcounter = memcounter+1

if finished == True:
    print("\nProgram Halted")
else:
    print("\nAll code in memory has been executed")
print(f"\nDONE!\nLines excecuted:{memcounter}")