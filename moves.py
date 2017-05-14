# ################### Movetables describe the transformation of the coordinates by cube moves. #########################

from os import path
import array as ar
import cubie as cb
import enums
from defs import N_TWIST, N_CORNERS, N_MOVE

a = cb.CubieCube()
# ############################ Move table for the the corners. ##################################

# The twist coordinate describes the 3^6 = 729 possible orientations of the 8 corners
fname = "move_corntwist"
print("creating " + fname + " table...")
corntwist_move = ar.array('H', [0 for i in range(N_TWIST * N_MOVE)])
for i in range(N_TWIST):
    a.set_cornertwist(i)
    for j in (enums.Color.U, enums.Color.R, enums.Color.F):  # three faces U, R, F
        for k in range(3):  # three moves for each face, for example U, U2, U3 = U'
            a.multiply(cb.basicMoveCube[j])
            corntwist_move[N_MOVE * i + 3 * j + k] = a.get_corntwist()
        a.multiply(cb.basicMoveCube[j])  # 4. move restores face


# The corners coordinate describes the 7! = 5040 permutations of the corners.
fname = "move_cornperm"
if not path.isfile(fname):
    print("creating " + fname + " table...")
    cornperm_move = ar.array('H', [0 for i in range(N_CORNERS * N_MOVE)])
    # Move table for the corners. corner  < 40320
    for i in range(N_CORNERS):
        if (i+1) % 200 == 0:
            print('.', end='', flush=True)
        a.set_corners(i)
        for j in (enums.Color.U, enums.Color.R, enums.Color.F):  # three faces U, R, F
            for k in range(3):
                a.multiply(cb.basicMoveCube[j])
                cornperm_move[N_MOVE * i + 3 * j + k] = a.get_cornperm()
            a.multiply(cb.basicMoveCube[j])
    fh = open(fname, "wb")
    cornperm_move.tofile(fh)
    fh.close()
    print()
else:
    print("loading " + fname + " table...")
    fh = open(fname, "rb")
    cornperm_move = ar.array('H')
    cornperm_move.fromfile(fh, N_CORNERS * N_MOVE)
fh.close()
########################################################################################################################
