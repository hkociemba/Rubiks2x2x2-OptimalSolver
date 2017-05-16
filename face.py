# ####### The 2x2x2 cube on the facelet level is described by positions of the colored stickers. #######################

from defs import cornerFacelet, cornerColor
from enums import Color, Corner
from cubie import CubieCube, CUBE_OK


class FaceCube:
    """Represents a 2x2x2 cube on the facelet level with 24 colored facelets."""
    def __init__(self):
        self.f = []
        for i in range(4):
            self.f.append(Color.U)
        for i in range(4):
            self.f.append(Color.R)
        for i in range(4):
            self.f.append(Color.F)
        for i in range(4):
            self.f.append(Color.D)
        for i in range(4):
            self.f.append(Color.L)
        for i in range(4):
            self.f.append(Color.B)

    def __str__(self):
        return self.to_string()

    def from_string(self, s):
        """Constructs a facelet cube from a string. See class Facelet(IntEnum) in enums.py for string format.
        
        The color scheme is detected automatically.
        """
        if len(s) < 24:
            return 'Error: Cube definition string ' + s + ' contains less than 24 facelets.'
        elif len(s) > 24:
            return 'Error: Cube definition string ' + s + ' contains more than 24 facelets.'
        cnt = [0] * 6
        for i in range(24):
            if s[i] == 'U':
                self.f[i] = Color.U
                cnt[Color.U] += 1
            elif s[i] == 'R':
                self.f[i] = Color.R
                cnt[Color.R] += 1
            elif s[i] == 'F':
                self.f[i] = Color.F
                cnt[Color.F] += 1
            elif s[i] == 'D':
                self.f[i] = Color.D
                cnt[Color.D] += 1
            elif s[i] == 'L':
                self.f[i] = Color.L
                cnt[Color.L] += 1
            elif s[i] == 'B':
                self.f[i] = Color.B
                cnt[Color.B] += 1
        if all(x == 4 for x in cnt):
            # remap colors if necessary
            col = [self.f[cornerFacelet[Corner.DBL][i]] for i in range(3)]  # colors of the DBL-corner
            map_col = [-1] * 6
            for i in range(3):
                map_col[col[i]] = cornerColor[Corner.DBL][i]  # map colors to right colors
            # now remap the remaining colors, try all possibilites
            a = ((Color.U, Color.R, Color.F), (Color.U, Color.F, Color.R), (Color.R, Color.U, Color.F),
                 (Color.R, Color.F, Color.U), (Color.F, Color.U, Color.R), (Color.F, Color.R, Color.U))
            empty = []
            for i in Color:
                if map_col[i] == -1:
                    empty.append(i)  # empty contains the 3 indices of the yet nonmapped colors
            fsave = self.f[:]
            for c in a:
                for i in range(3):
                    map_col[empty[i]] = c[i]
                self.f = fsave[:]
                for i in range(24):
                    self.f[i] = map_col[self.f[i]]  # remap the colors
                cc = self.to_cubie_cube()
                s = cc.verify()
                if s == CUBE_OK:
                    return True

            return 'Error: Facelet configuration does not define a valid cube.'
        else:
            return 'Error: Cube definition string ' + s + ' does not contain exactly 4 facelets of each color.'



    def to_string(self):
        """Gives string representation of the facelet cube."""
        s = ''
        for i in range(24):
            if self.f[i] == Color.U:
                s += 'U'
            elif self.f[i] == Color.R:
                s += 'R'
            elif self.f[i] == Color.F:
                s += 'F'
            elif self.f[i] == Color.D:
                s += 'D'
            elif self.f[i] == Color.L:
                s += 'L'
            elif self.f[i] == Color.B:
                s += 'B'
        return s

    def to_cubie_cube(self):
        """Returns a cubie representation of the facelet cube."""
        cc = CubieCube()
        cc.cp = [-1] * 8  # invalidate corner permutation
        for i in Corner:
            col0 = None
            fac = cornerFacelet[i]  # facelets of corner  at position i
            for ori in range(3):
                if self.f[fac[ori]] == Color.U or self.f[fac[ori]] == Color.D:
                    col0 = self.f[fac[ori]]
                    break
            col1 = self.f[fac[(ori + 1) % 3]]  # colors which identify the corner at position i
            col2 = self.f[fac[(ori + 2) % 3]]
            for j in Corner:
                col = cornerColor[j]  # colors of corner j
                if col0 != None and col0 == col[0] and col1 == col[1] and col2 == col[2]:
                    cc.cp[i] = j  # we have corner j in corner position i
                    cc.co[i] = ori
                    break
        return cc
