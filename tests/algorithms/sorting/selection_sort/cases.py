"""Sample inputs and expected steps for selection-sort algorithm tests."""

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject

INPUT_DATA_SYNC_TEST: list[int] = [5, 89, 25, 42, 1, 5, 8, 14, 0, -2, 3]
"""Fixed list for the selection-sort golden step sequence."""

EXPECTED_DATA_SYNC_TEST: list[BaseSortStepValueObject] = [
    BaseSortStepValueObject(
        0, 5, (5, 89, 25, 42, 1, 5, 8, 14, 0, -2, 3), (-2, 89, 25, 42, 1, 5, 8, 14, 0, 5, 3), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        1, 89, (-2, 89, 25, 42, 1, 5, 8, 14, 0, 5, 3), (-2, 0, 25, 42, 1, 5, 8, 14, 89, 5, 3), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        2, 25, (-2, 0, 25, 42, 1, 5, 8, 14, 89, 5, 3), (-2, 0, 1, 42, 25, 5, 8, 14, 89, 5, 3), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        3, 42, (-2, 0, 1, 42, 25, 5, 8, 14, 89, 5, 3), (-2, 0, 1, 3, 25, 5, 8, 14, 89, 5, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        4, 25, (-2, 0, 1, 3, 25, 5, 8, 14, 89, 5, 42), (-2, 0, 1, 3, 5, 25, 8, 14, 89, 5, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        5, 25, (-2, 0, 1, 3, 5, 25, 8, 14, 89, 5, 42), (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        6, 8, (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        7, 14, (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        8, 89, (-2, 0, 1, 3, 5, 5, 8, 14, 89, 25, 42), (-2, 0, 1, 3, 5, 5, 8, 14, 25, 89, 42), SortingStatus.SORTING
    ),
    BaseSortStepValueObject(
        9, 89, (-2, 0, 1, 3, 5, 5, 8, 14, 25, 89, 42), (-2, 0, 1, 3, 5, 5, 8, 14, 25, 42, 89), SortingStatus.READY
    ),
]
"""Exact steps expected for ``INPUT_DATA_SYNC_TEST``."""
