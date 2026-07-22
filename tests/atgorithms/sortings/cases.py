"""Sample arrays for sorting algorithm tests."""

from random import randint

NOT_SORTED_ARRAYS: tuple[tuple[int, ...], ...] = (
    (5, 4, 3, 2, 1),
    (3, 4, 1, 5, 2),
    (3, 4, 1, 1, 5, 2, 2),
    (2, 2, 2),
    (1,),
    tuple(randint(i, 100) for i in range(1, 101)),
    (),
)
"""Unsorted and edge-case arrays for insertion-sort tests."""
