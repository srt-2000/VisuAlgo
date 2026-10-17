"""Sample inputs and expected steps for insertion-sort algorithm tests."""

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject

INPUT_DATA_SYNC_TEST: list[int] = [1, 3, 2, 5]
"""Fixed list for the insertion-sort golden step sequence."""

EXPECTED_DATA_SYNC_TEST: list[BaseSortStepValueObject] = [
    BaseSortStepValueObject(0, 1, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 3, (1, 3, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(2, 2, (1, 3, 2, 5), (1, 2, 3, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(3, 5, (1, 2, 3, 5), (1, 2, 3, 5), SortingStatus.READY),
]
"""Exact steps expected for ``INPUT_DATA_SYNC_TEST``."""
