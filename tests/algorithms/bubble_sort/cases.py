"""Sample inputs and expected steps for bubble-sort algorithm tests."""

from random import randint

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject

NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE: tuple[list[int], ...] = (
    [5, 4, 3, 2, 1],
    [3, 4, 1, 5, 2],
    [3, 4, 1, 1, 5, 2, 2],
    [2, 2, 2],
    [5, 2, 3, 5, 10, 10, 3],
    [randint(i, 100) for i in range(1, 101)],
)
"""Lists of length 2+ used to check that ``iter_steps`` behave correctly."""

BUBLE_SORT_DATA_SYNC_TEST: list[int] = [5, 3, 1, 2]
"""Fixed list for the bubble-sort golden step sequence."""

BUBBLE_SORT_EXPECTED_DATA_SYNC_TEST: list[BaseSortStepValueObject] = [
    BaseSortStepValueObject(0, 5, (5, 3, 1, 2), (3, 5, 1, 2), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 5, (3, 5, 1, 2), (3, 1, 5, 2), SortingStatus.SORTING),
    BaseSortStepValueObject(2, 5, (3, 1, 5, 2), (3, 1, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(0, 3, (3, 1, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 3, (1, 3, 2, 5), (1, 2, 3, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(0, 1, (1, 2, 3, 5), (1, 2, 3, 5), SortingStatus.READY),
]
"""Exact steps expected for ``BUBLE_SORT_DATA_SYNC_TEST``."""
