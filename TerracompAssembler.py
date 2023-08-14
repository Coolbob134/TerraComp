#"Assembler" for the Terracomp project
#GitHub: https://github.com/Coolbob134/TerraComp/ (currently private)

#This compiler will only compile into usable machine code at the moment. The user still needs to write the program into program memory manually.

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
if input("Do you want to write the output to a file? Y/N: ") == 'Y':
    writetofile = True
    OutputFile = open(input("Enter Output file path: "),"w")
    
    
def assemble(inputline):
    line1 = inputline.strip()  
    cmd = line1.split(" ")[0]
    if cmd not in commands:
        raise ValueError(f"{cmd} is not a valid command (line {linecounter})")    
    if len(line1.split(" ")) == command_arguments[cmd]:
        if len(line1.split(" ")) == 2:
            arg1 = line1.split(" ")[1]
        else:
            arg1 = 0
        line1 = commands[cmd]
        if int(arg1) <= 15:
            line1 = line1 + " " + f"{int(arg1):04b}"
        else:
            raise ValueError(f"Value exceeds maximum at line {linecounter}")
    else:
        raise ValueError(f"Incorrect number of arguments at line {linecounter}") 
    return line1

with open(filepath) as SourceFile:
    for line in SourceFile.readlines():
        linecounter = linecounter +1
        print(assemble(line))
        if writetofile == True:
            OutputFile.write(assemble(line)+"\r")

print("\nDONE!")
