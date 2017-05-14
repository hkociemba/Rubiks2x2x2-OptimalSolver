# ######### The 2x2x2 cube on the cubie level is described by the permutation and orientations of the corners ##########

from defs import cornerFacelet, cornerColor, N_CORNERS, N_TWIST
from enums import Color, Corner as Co
import face
from misc import rotate_left, rotate_right
from random import randrange

# ################## the basic six cube moves described by permutations and changes in orientation #####################

# Up-move
cpU = [Co.UBR, Co.URF, Co.UFL, Co.ULB,  Co.DRB, Co.DFR, Co.DLF, Co.DBL]
coU = [0, 0, 0, 0, 0, 0, 0, 0]

# Right-move
cpR = [Co.DFR, Co.UFL, Co.ULB, Co.URF, Co.UBR, Co.DRB, Co.DLF, Co.DBL]  # permutation of the corners
coR = [2, 0, 0, 1, 2, 1, 0, 0]  # changes of the orientations of the corners

# Front-move
cpF = [Co.UFL, Co.DLF, Co.ULB, Co.UBR, Co.DRB, Co.URF, Co.DFR, Co.DBL]
coF = [1, 2, 0, 0, 0, 2, 1, 0]

########################################################################################################################

CUBE_OK = True


class CubieCube:
    """Represents a 2x2x2 cube on the cubie level with 8 corner cubies and the corner orientations.

    Is also used to represent the 18 cube moves.
    """

    def __init__(self, cp=None, co=None):
        """
        Initializes corners and edges.
        :param cp: corner permutation
        :param co: corner orientation
        """
        if cp is None:
            self.cp = [Co(i) for i in range(8)]  # You may not put this as the default two lines above!
        else:
            self.cp = cp[:]
        if co is None:
            self.co = [0] * 8
        else:
            self.co = co[:]

    def __str__(self):
        """Prints string for a cubie cube."""
        s = ''
        for i in Co:
            s = s + '(' + str(self.cp[i]) + ',' + str(self.co[i]) + ')'
        return s

    def __eq__(self, other):
        """Defines equality of two cubie cubes."""
        if self.cp == other.cp and self.co == other.co:
            return True
        else:
            return False

    def to_facelet_cube(self):
        """Returns a facelet representation of the cube."""
        fc = face.FaceCube()
        for i in Co:
            j = self.cp[i]  # corner j is at corner position i
            ori = self.co[i]  # orientation of C j at position i
            for k in range(3):
                fc.f[cornerFacelet[i][(k + ori) % 3]] = cornerColor[j][k]
        return fc

    def multiply(self, b):
        """Multiplies this cubie cube with another cubie cube b. Does not change b."""
        c_perm = [0] * 8
        c_ori = [0] * 8
        ori = 0
        for c in Co:
            c_perm[c] = self.cp[b.cp[c]]
            ori_a = self.co[b.cp[c]]
            ori_b = b.co[c]
            if ori_a < 3 and ori_b < 3:  # two regular cubes
                ori = ori_a + ori_b
                if ori >= 3:
                    ori -= 3
            elif ori_a < 3 <= ori_b:  # cube b is in a mirrored state
                ori = ori_a + ori_b
                if ori >= 6:
                    ori -= 3  # the composition also is in a mirrored state
            elif ori_a >= 3 > ori_b:  # cube a is in a mirrored state
                ori = ori_a - ori_b
                if ori < 3:
                    ori += 3  # the composition is a mirrored cube
            elif ori_a >= 3 and ori_b >= 3:  # if both cubes are in mirrored states
                ori = ori_a - ori_b
                if ori < 0:
                    ori += 3  # the composition is a regular cube
            c_ori[c] = ori
        for c in Co:
            self.cp[c] = c_perm[c]
            self.co[c] = c_ori[c]

    def inv_cubie_cube(self, d):
        """Stores the inverse of this cubie cube in d."""

        for c in Co:
            d.cp[self.cp[c]] = c
        for c in Co:
            ori = self.co[d.cp[c]]
            if ori >= 3:
                d.co[c] = ori
            else:
                d.co[c] = -ori
                if d.co[c] < 0:
                    d.co[c] += 3


    # ###################################### coordinates for 2x2x2 cube #################################################
    def get_corntwist(self):
        """The twist of the 8 corners. 0 <= twist < 729. The DBL-corner is fixed."""
        ret = 0
        for i in range(Co.URF, Co.DLF):
            ret = 3 * ret + self.co[i]
        return ret

    def set_cornertwist(self, twist):
        twistparity = 0
        for i in range(Co.DLF - 1, Co.URF - 1, -1):
            self.co[i] = twist % 3
            twistparity += self.co[i]
            twist //= 3
        self.co[Co.DLF] = ((3 - twistparity % 3) % 3)


    def get_cornperm(self):
        """The permutation of the 8 corners. 0 <= corners < 5040. The DLB_corner is fixed."""
        perm = list(self.cp)  # duplicate cp
        b = 0
        for j in range(Co.DBL, Co.URF, -1):
            k = 0
            while perm[j] != j:
                rotate_left(perm, 0, j)
                k += 1
            b = (j + 1) * b + k
        return b

    def set_corners(self, idx):

        self.cp = [i for i in Co]
        for j in Co:
            k = idx % (j + 1)
            idx //= j + 1
            while k > 0:
                rotate_right(self.cp, 0, j)
                k -= 1
                # ############################## end coordinates for 2x2x2 cube ########################################

                # #################################### other usefull functions #########################################

    def randomize(self):
        """Generates a random cube. The probability is the same for all possible states."""
        self.set_corners(randrange(N_CORNERS))
        self.set_cornertwist(randrange(N_TWIST))

    def verify(self):
        """Checks if cubiecube is valid"""

        corner_count = [0] * 8
        for i in Co:
            corner_count[self.cp[i]] += 1
        for i in Co:
            if corner_count[i] != 1:
                return 'Error: Some corners are undefined.'

        s = 0
        for i in Co:
            s += self.co[i]
        if s % 3 != 0:
            return 'Error: Total corner twist is wrong.'

        return CUBE_OK


########################################################################################################################

# ################################## these cubes represent the basic cube moves ########################################
basicMoveCube = [0] * 6
basicMoveCube[Color.U] = CubieCube(cpU, coU)
basicMoveCube[Color.R] = CubieCube(cpR, coR)
basicMoveCube[Color.F] = CubieCube(cpF, coF)
########################################################################################################################

# ################################# these cubes represent the all 9 cube moves ########################################
moveCube = [0] * 9
for c1 in [Color.U, Color.R, Color.F]:
    cc = CubieCube()
    for k1 in range(3):
        cc.multiply(basicMoveCube[c1])
        moveCube[3 * c1 + k1] = CubieCube(cc.cp, cc.co)
########################################################################################################################
