#Assembler for the Terracomp project
#GitHub: https://github.com/Coolbob134/TerraComp/ (currently public)

#This assembler will only convert into usable machine code at the moment. The user still needs to write the program into program memory manually. 
#The output file option can be used to excecute the generated code in the simulator.

import os.path

commands = {
    "STA"  : "0001",
    "STB"  : "0010",
    "STC"  : "0011",
    "ADD"  : "0100",
    "DISP" : "0101",
    "MOVA" : "0110",
    "MOVB" : "0111"
}
command_arguments = {
    "STA"  : 2,
    "STB"  : 2,
    "STC"  : 2,
    "ADD"  : 1,
    "DISP" : 1,
    "MOVA" : 1,
    "MOVB" : 1    
}
linecounter = 0
writetofile = False

print("TERRACOMP ASSEMBLER\n")
filepath = input("Enter file path: ")
if not os.path.exists(filepath):
    raise Exception(f"File \"{filepath}\" does not exist")
if input("Do you want to write the output to a file? Y/N: ") == 'Y':
    writetofile = True
    OutputFilePath = input("Enter Output file path: ")
    if not os.path.exists(filepath):
        raise Exception(f"File \"{filepath}\" does not exist")
    OutputFile = open(OutputFilePath,"w")
    
    
def assemble(inputline):
    global linecounter
    line = inputline.strip()  
    cmd = line.split(" ")[0]
    if cmd not in commands:
        raise SyntaxError(f"{cmd} is not a valid command (line {linecounter})")    
    if len(line.split(" ")) == command_arguments[cmd]:
        if len(line.split(" ")) == 2:
            arg1 = line.split(" ")[1]
        else:
            arg1 = 0
        line = commands[cmd]
        if int(arg1) <= 15:
            line = line + " " + f"{int(arg1):04b}"
        else:
            raise ValueError(f"Value exceeds maximum at line {linecounter}")
    else:
        raise SyntaxError(f"Incorrect number of arguments at line {linecounter}") 
    return line

with open(filepath) as SourceFile:
    for line in SourceFile.readlines():
        linecounter = linecounter +1
        print(assemble(line))
        if writetofile == True:
            OutputFile.write(assemble(line)+"\n")

print("\nDONE!")
