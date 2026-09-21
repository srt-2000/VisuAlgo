"""Parametrized limits for ``get_not_sorted_random_list`` tests."""
from collections import defaultdict

from backend.utils.constants import SortingStatus

RANDOM_NOT_ZERO_LIST_LIMITS: tuple[tuple[int, int, int], ...] = (
    (10, 1, 10),
    (10, 1, 101),
    (101, 1, 10),
    (101, 10, 10),
    (101, 1, 1),
    (10, -101, 101),
    (1, -101, 101),
)
"""``(length, min_value, max_value)`` cases with a non-empty result."""

RANDOM_ZERO_ELEMENTS_LIST: tuple[tuple[int, int, int], ...] = (
    (0, -10, 10),
    (0, 0, 10),
    (0, 1, 10),
    (0, 10, 10),
)
"""``(length, min_value, max_value)`` cases that must return ``[]``."""

INDEXES_AND_STATUS_RESULTS: tuple[tuple[int, int, str],...] = (
    (1, 3, SortingStatus.SORTING),
    (0, 678, SortingStatus.SORTING),
    (0, 0, SortingStatus.READY),
    (2, 2, SortingStatus.READY),
    (-1, 1, SortingStatus.SORTING),
    (-1, 0, SortingStatus.SORTING),
    (-1, -1, SortingStatus.READY)
)

DATAFRAME_TEST_INVARIANTS: tuple[defaultdict[str, list[str]], ...] = (
    defaultdict(list, {
        "column1": ["par1_1", "par1_2", "par1_3"]
    }),
    defaultdict(list, {
        "middle index": ["0", "2", "3"],
        "check status to": [">", "<", "="],
        "target": ["7", "7", "7"],
    }),
    defaultdict(list, {
        "step range": ["1 ... 10"],
        "range size": ["10 pieces"],
        "middle index": ["5"],
        "middle element": ["5"],
        "check status to": ["="],
        "target": ["5"],
    }),
)
"""Non-empty column→values maps; all value lists in a case share one length."""
