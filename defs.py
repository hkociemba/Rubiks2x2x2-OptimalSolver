 ###################################### some definitions and constants ################################################

from enums import Facelet as Fc, Color as Cl

# Map the corner positions to facelet positions.
cornerFacelet = [[Fc.U4, Fc.R1, Fc.F2], [Fc.U3, Fc.F1, Fc.L2], [Fc.U1, Fc.L1, Fc.B2], [Fc.U2, Fc.B1, Fc.R2],
                 [Fc.D4, Fc.R4, Fc.B3], [Fc.D2, Fc.F4, Fc.R3], [Fc.D1, Fc.L4, Fc.F3], [Fc.D3, Fc.B4, Fc.L3],
                 ]


# Map the corner positions to facelet colors.
cornerColor = [[Cl.U, Cl.R, Cl.F], [Cl.U, Cl.F, Cl.L], [Cl.U, Cl.L, Cl.B], [Cl.U, Cl.B, Cl.R],
               [Cl.D, Cl.R, Cl.B], [Cl.D, Cl.F, Cl.R], [Cl.D, Cl.L, Cl.F], [Cl.D, Cl.B, Cl.L]
               ]


# ###################################### some "constants" ##############################################################
N_MOVE = 9  # number of possible face moves
N_TWIST = 729  # 3^6 possible corner orientations
N_CORNERS = 5040  # 7! corner permutations in phase 2
########################################################################################################################
