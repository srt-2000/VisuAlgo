"""Parametrized inputs for utils unit tests (random lists, status, keys)."""

from typing import Any

from backend.domains.constants import SortingStatus

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

INDEXES_AND_STATUS_RESULTS: tuple[tuple[int, int, str], ...] = (
    (1, 3, SortingStatus.SORTING),
    (0, 678, SortingStatus.SORTING),
    (0, 0, SortingStatus.READY),
    (2, 2, SortingStatus.READY),
    (-1, 1, SortingStatus.SORTING),
    (-1, 0, SortingStatus.SORTING),
    (-1, -1, SortingStatus.READY),
)
"""``(current index, last index, expected status)`` cases."""

UNDERSCORE_REMOVING_DATA_SET: tuple[dict[str, Any], ...] = (
    {"with_underscore": [1, 2, 3]},
    {"with no underscore": [1, 2, 3]},
    {" ": [1, 2, 3]},
    {"_": [1, 2, 3]},
    {"0_1": [1, 2, 3]},
    {
        "s_S": [1, 2, 3],
        "before_after on": [1, 2, 3],
        "free teo get_ao": [1, 2, 3],
    },
)
"""Dict samples for underscore-to-space key cleanup tests."""
