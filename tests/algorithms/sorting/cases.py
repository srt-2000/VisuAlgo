"""Shared sample arrays for sorting algorithm unit tests."""

from random import randint

NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE: tuple[list[int], ...] = (
    [5, 4, 3, 2, 1],
    [3, 4, 1, 5, 2],
    [3, 4, 1, 1, 5, 2, 2],
    [2, 2, 2],
    [5, 2, 3, 5, 10, 10, 3],
    [randint(i, 100) for i in range(1, 101)],
)
"""Lists of length 2+ used to check that ``iter_steps`` behaves correctly."""
