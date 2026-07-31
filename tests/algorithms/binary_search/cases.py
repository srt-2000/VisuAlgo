"""Sample inputs and expected steps for binary-search algorithm tests."""

from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus

FILLED_LIST_EXPECTED_RESULTS: tuple[tuple[int, int | None], ...] = (
    (3, 2),
    (9, 8),
    (7, 6),
)
"""``(target, expected_index)`` pairs for values that exist in ``[1..9]``."""

FILLED_LIST_TARGET_NONE_RESULTS: int = 10
"""Target that is missing from ``[1..9]`` and must return ``None``."""

BINARY_SEARCH_ITER_STEPS_INVARIANTS: tuple[tuple[list[int], int], ...] = (
    ([], 2),
    ([7], 7),
    ([7], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4),
    ([2, 2, 2], 2),
    ([1, 3, 5], 2),
)
"""``(array, target)`` pairs used to check ``iter_steps`` rules."""

BINARY_SEARCH_DATA_SYNC_TEST: tuple[list[int], int] = ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
"""Fixed ``(array, target)`` for the golden step sequence."""

BINARY_SEARCH_EXPECTED_DATA_SYNC_TEST: list[BinarySearchStepValueObject] = [
    BinarySearchStepValueObject(0, 8, 4, 5, BinarySearchStatus.GREATER, 3),
    BinarySearchStepValueObject(0, 3, 1, 2, BinarySearchStatus.LESS, 3),
    BinarySearchStepValueObject(2, 3, 2, 3, BinarySearchStatus.EQUAL, 3),
]
"""Exact steps expected for ``BINARY_SEARCH_DATA_SYNC_TEST``."""
