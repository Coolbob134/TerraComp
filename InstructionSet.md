# INSTRUCTION SET
## DESCRIPTION

    The instruction set currently has 7 instructions.

## INSTRUCTIONS

    OPCODE    |  DESCRIPTION                                                                     |  BINARY  |  SYNTAX
    
    1)  STA	  |  Stores value in register A                                                      |  0001    |  STA [VALUE]
    2)  STB	  |  Stores value in register B                                                      |  0010    |  STB [VALUE]
    3)  STC	  |  Stores value in register C                                                      |  0011    |  STB [VALUE]
    4)  ADD	  |  Adds the values stored in register A and B and stores the result in register C  |  0100    |  ADD
    5)  DISP  |  Displays value stored in register C                                             |  0101    |  DISP
    6)  MOVA  |  Moves the value of register C to register A                                     |  0110    |  MOVA
    7)  MOVB  |  Moves the value of register C to register B                                     |  0111    |  MOVB

## USAGE

    The instruction memory is bundled in 8 bit memory 'cells'. Each 8-bit 'cell' is split into two more 4-bit 'cells'. 
    The first four bits represent the instruction. The last four bits contains the value for the instruction.
    
    An example: 00110001 - The first four bits (0011) represent STC. 
                         -The last four bits (0001) represent the value to be stored in register C.
