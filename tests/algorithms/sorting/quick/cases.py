"""Sample inputs and expected steps for quick-sort algorithm tests."""

from backend.domains.constants import SortingStatus
from backend.domains.sorting import QuickSortStepValueObject

INPUT_DATA_SYNC_TEST: list[int] = [45, -2, 5, 3, 0, 1, -1, -1, 2]
"""Fixed list for the quick-sort golden step sequence."""

TWO_ELEMENT_ARRAY: list[int] = [2, 1]
"""Minimal non-trivial partition case."""

ALREADY_SORTED_ARRAY: list[int] = [1, 2, 3, 4, 5]
"""Already sorted input for tree-shape coverage."""

EXPECTED_DATA_SYNC_TEST: list[QuickSortStepValueObject] = [
    QuickSortStepValueObject(
        depth=0,
        side="root",
        pivot=0,
        before=(45, -2, 5, 3, 0, 1, -1, -1, 2),
        result=([-2, -1, -1], [0], [45, 5, 3, 1, 2]),
        status=SortingStatus.SORTING,
    ),
    QuickSortStepValueObject(
        depth=1, side="left", pivot=-1, before=(-2, -1, -1), result=([-2], [-1, -1], []), status=SortingStatus.SORTING
    ),
    QuickSortStepValueObject(
        depth=1,
        side="right",
        pivot=3,
        before=(45, 5, 3, 1, 2),
        result=([1, 2], [3], [45, 5]),
        status=SortingStatus.SORTING,
    ),
    QuickSortStepValueObject(
        depth=2, side="left", pivot=2, before=(1, 2), result=([1], [2], []), status=SortingStatus.SORTING
    ),
    QuickSortStepValueObject(
        depth=2, side="right", pivot=5, before=(45, 5), result=([], [5], [45]), status=SortingStatus.SORTING
    ),
    QuickSortStepValueObject(
        depth=0,
        side="root",
        pivot=0,
        before=(45, -2, 5, 3, 0, 1, -1, -1, 2),
        result=(
            [-2, -1, -1],
            [0],
            [1, 2, 3, 5, 45],
        ),
        status=SortingStatus.READY,
    ),
]
"""Exact steps expected for ``INPUT_DATA_SYNC_TEST``."""
