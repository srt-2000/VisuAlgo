"""Parametrized limits for ``get_not_sorted_random_list`` tests."""

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
