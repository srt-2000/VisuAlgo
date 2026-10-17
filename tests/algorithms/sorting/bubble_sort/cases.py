"""Sample inputs and expected steps for bubble-sort algorithm tests."""

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject

INPUT_DATA_SYNC_TEST: list[int] = [5, 3, 1, 2]
"""Fixed list for the bubble-sort golden step sequence."""

EXPECTED_DATA_SYNC_TEST: list[BaseSortStepValueObject] = [
    BaseSortStepValueObject(0, 5, (5, 3, 1, 2), (3, 5, 1, 2), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 5, (3, 5, 1, 2), (3, 1, 5, 2), SortingStatus.SORTING),
    BaseSortStepValueObject(2, 5, (3, 1, 5, 2), (3, 1, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(0, 3, (3, 1, 2, 5), (1, 3, 2, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(1, 3, (1, 3, 2, 5), (1, 2, 3, 5), SortingStatus.SORTING),
    BaseSortStepValueObject(0, 1, (1, 2, 3, 5), (1, 2, 3, 5), SortingStatus.READY),
]
"""Exact steps expected for ``INPUT_DATA_SYNC_TEST``."""
