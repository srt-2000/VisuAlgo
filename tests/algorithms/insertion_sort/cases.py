"""Sample inputs and expected steps for insertion-sort algorithm tests."""

from random import randint

from backend.domains.sorting import InsertionSortStepValueObject
from backend.utils.constants import SortingStatus

NOT_SORTED_ARRAYS: tuple[list[int], ...] = (
    [5, 4, 3, 2, 1],
    [3, 4, 1, 5, 2],
    [3, 4, 1, 1, 5, 2, 2],
    [2, 2, 2],
    [1],
    [randint(i, 100) for i in range(1, 101)],
)
"""Lists used to check that ``sort`` and ``iter_steps`` behave correctly."""

INSERTION_SORT_DATA_SYNC_TEST: list[int] = [1, 3, 2, 5]
"""Fixed list for the golden step sequence."""

INSERTION_SORT_EXPECTED_DATA_SYNC_TEST: list[InsertionSortStepValueObject] = [
    InsertionSortStepValueObject(
        0, 1, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING
    ),
    InsertionSortStepValueObject(
        1, 3, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING
    ),
    InsertionSortStepValueObject(
        2, 2, (1, 3, 2, 5), (1, 2, 3, 5), SortingStatus.SORTING
    ),
    InsertionSortStepValueObject(
        3, 5, (1, 2, 3, 5), (1, 2, 3, 5), SortingStatus.READY
    ),
]
"""Exact steps expected for ``INSERTION_SORT_DATA_SYNC_TEST``."""
