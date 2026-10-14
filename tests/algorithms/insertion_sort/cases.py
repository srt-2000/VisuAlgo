"""Sample inputs and expected steps for insertion-sort algorithm tests."""

from random import randint

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject

NOT_SORTED_ARRAYS: tuple[list[int], ...] = (
    [5, 4, 3, 2, 1],
    [3, 4, 1, 5, 2],
    [3, 4, 1, 1, 5, 2, 2],
    [2, 2, 2],
    [1],
    [randint(i, 100) for i in range(1, 101)],
)
"""Lists used to check that ``iter_steps`` behaves correctly."""

SORT_DATA_SYNC_TEST: list[int] = [1, 3, 2, 5]
"""Fixed list for the insertion-sort golden step sequence."""

INSERTION_SORT_EXPECTED_DATA_SYNC_TEST: list[BaseSortStepValueObject] = [
    BaseSortStepValueObject(0, 1, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 3, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(2, 2, (1, 3, 2, 5), (1, 2, 3, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(3, 5, (1, 2, 3, 5), (1, 2, 3, 5), SortingStatus.READY),
]
"""Exact steps expected for ``SORT_DATA_SYNC_TEST``."""
