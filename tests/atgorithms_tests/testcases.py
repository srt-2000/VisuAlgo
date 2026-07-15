"""Shared test input constants for algorithm unit tests."""

from random import randint

from domains.binary_search import BinarySearchStatus, BinarySearchStepValueObject

NOT_SORTED_ARRAYS: tuple[tuple[int, ...], ...] = (
    (5, 4, 3, 2, 1),
    (3, 4, 1, 5, 2),
    (3, 4, 1, 1, 5, 2, 2),
    (2, 2, 2),
    (1,),
    tuple(randint(i, 100) for i in range(1, 101)),
    (),
)
"""Unsorted (and edge) arrays used to parametrize insertion sort tests."""

BINARY_SEARCH_ITER_STEPS_INVARIANTS: tuple[tuple[list[int], int], ...] = (
    ([], 2),
    ([7], 7),
    ([7], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4),
    ([2, 2, 2], 2),
    ([1, 3, 5], 2),
)
"""``(array, target)`` pairs for ``iter_steps`` invariant checks."""

INPUT_DATA_SYNC_TEST: tuple[list[int], int] = ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
"""Fixed ``(array, target)`` input for the golden ``iter_steps`` sequence."""

EXPECTED_DATA_SYNC_TEST: list[BinarySearchStepValueObject] = [
    BinarySearchStepValueObject(0, 8, 4, 5, BinarySearchStatus.GREATER, 3),
    BinarySearchStepValueObject(0, 3, 1, 2, BinarySearchStatus.LESS, 3),
    BinarySearchStepValueObject(2, 3, 2, 3, BinarySearchStatus.EQUAL, 3),
]
"""Expected step sequence for ``INPUT_DATA_SYNC_TEST``."""
