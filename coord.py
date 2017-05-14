# ####### The cube on the coordinate level is described by a 3-tuple of natural numbers in phase 1 and phase 2. ########

import moves as mv
from defs import N_MOVE

SOLVED = 0  # 0 is index of solved state (except for u_edges coordinate)


class CoordCube:
    """Represents a 2x2x2 cube on the coordinate level.

    A state is uniquely determined by the coordinates corntwist and cornperm.
    """

    def __init__(self, cc=None):
        if cc is None:
            self.corntwist = SOLVED  # twist of corners
            self.cornperm = SOLVED  # permutation of corners
        else:
            self.corntwist = cc.get_corntwist()
            self.cornperm = cc.get_cornperm()

    def __str__(self):
        s = '(corntwist: ' + str(self.corntwist) + ', cornperm: ' + str(self.cornperm) + ')'
        return s

    def move(self, m):
        self.corntwist = mv.twist_move[N_MOVE * self.corntwist + m]
        self.cornperm = mv.corners_move[N_MOVE * self.cornperm + m]
########################################################################################################################

