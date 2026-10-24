"""Precompiled move continuations for the fixed-corner HTM generator set."""

from enums import Move


# After a U, R, or F move, all three turns of that same face are redundant.
# Building these six-move tuples once avoids testing nine candidates at every
# non-root search node.
LEGAL_NEXT_MOVES = tuple(
    tuple(move for move in Move if move // 3 != previous // 3)
    for previous in Move
)
