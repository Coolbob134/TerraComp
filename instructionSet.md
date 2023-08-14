# INSTRUCTION SET
## DESCRIPTION

    The instruction set currently has 7 instructions.

## INSTRUCTIONS

    OPCODE    |  DESCRIPTION                                                                     |  BINARY  |  SYNTAX
    
    1)  STA	  |  Stores value in register A                                                      |  0001    |  STA [VALUE]
    2)  STB	  |  Stores value in register B                                                      |  0010    |  STB [VALUE]
    3)  STC	  |  Stores value in register C                                                      |  0011    |  STB [VALUE]
    4)  ADD	  |  Adds the values stored in register A and B and stores the result in register C  |  0100    |  ADD
    5)  PRINT |  Displays value stored in register C                                             |  0101    |  DISP
    6)  MOVA  |  Moves the value of register C to register A                                     |  0110    |  MOVA
    7)  MOVB  |  Moves the value of register C to register B                                     |  0111    |  MOVB
