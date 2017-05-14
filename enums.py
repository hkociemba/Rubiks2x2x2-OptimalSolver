#  ####################  Enumerations which improve the readability of the code ########################################

from enum import IntEnum


class Facelet(IntEnum):
    """""
    The names of the facelet positions of the cube
              |********|
              |*U1**U2*|
              |********|
              |*U3**U4*|
              |********|
     |********|********|********|********|
     |*L1**L2*|*F1**F2*|*R1**R2*|*B1**B2*|
     |********|********|********|********|
     |*L3**L4*|*F3**F4*|*R3**R4*|*B3**B4*|
     |********|********|********|********|
              |********|
              |*D1**D2*|
              |********|
              |*D3**D4*|
              |********|
     

    A cube definition string "UBL..." means for example: In position U1 we have the U-color, in position U2 we have the
    B-color, in position U3 we have the L color etc. according to the order U1, U2, U3, U4, R1, R2, R3, R4, F1, F2, F3,
    F4, D1, D2, D3, D4, L1, L2, L3, L4, B1, B2, B3, B4 of the enum constants.
    """
    U1 = 0
    U2 = 1
    U3 = 2
    U4 = 3
    R1 = 4
    R2 = 5
    R3 = 6
    R4 = 7
    F1 = 8
    F2 = 9
    F3 = 10
    F4 = 11
    D1 = 12
    D2 = 13
    D3 = 14
    D4 = 15
    L1 = 16
    L2 = 17
    L3 = 18
    L4 = 19
    B1 = 20
    B2 = 21
    B3 = 22
    B4 = 23


class Color(IntEnum):
    """ The possible colors of the cube facelets. Color U refers to the color of the U(p)-face etc. 
    Also used to name the faces itself."""
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5


class Corner(IntEnum):
    """The names of the corner positions of the cube. Corner URF e.g. has an U(p), a R(ight) and a F(ront) facelet."""
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DRB = 4
    DFR = 5
    DLF = 6
    DBL = 7


class Move(IntEnum):
    """The moves in the faceturn metric. Not to be confused with the names of the facelet positions in class Facelet."""
    U1 = 0
    U2 = 1
    U3 = 2
    R1 = 3
    R2 = 4
    R3 = 5
    F1 = 6
    F2 = 7
    F3 = 8
