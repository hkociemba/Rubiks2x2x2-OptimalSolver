import unittest

import continuations as ct
from enums import Move


class ContinuationsTest(unittest.TestCase):
    def test_each_move_has_six_legal_continuations(self):
        for previous in Move:
            continuations = ct.LEGAL_NEXT_MOVES[previous]
            self.assertEqual(6, len(continuations))
            self.assertTrue(
                all(move // 3 != previous // 3 for move in continuations))

    def test_table_matches_original_condition(self):
        for previous in Move:
            expected = tuple(
                move for move in Move
                if move // 3 != previous // 3)
            self.assertEqual(
                expected, ct.LEGAL_NEXT_MOVES[previous])


if __name__ == '__main__':
    unittest.main()
