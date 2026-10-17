"""Helpers for random demo lists and the sorting-vs-ready label."""

from collections.abc import Iterable
from random import randint

from backend.domains.constants import SortingStatus


def get_not_sorted_random_list(
    length_limit: int,
    min_value: int,
    max_value: int,
) -> list[int]:
    """Build a list of random ints (usually unsorted).

    Args:
        length_limit: How many numbers to put in the list.
        min_value: Smallest allowed random number.
        max_value: Biggest allowed random number.

    Returns:
        A new list with ``length_limit`` random ints in
        ``[min_value, max_value]``. Empty if ``length_limit`` is ``0``.
    """
    random_list: list[int] = []
    list_range: Iterable[int] = range(length_limit)

    for _ in list_range:
        random_element: int = randint(min_value, max_value)
        random_list.append(random_element)

    return random_list


def get_current_sort_status(iter_position: int, max_pass_index: int) -> str:
    """Say whether this step is still sorting or already the last one.

    Args:
        iter_position: Index of the step we just finished.
        max_pass_index: Last pass index for this algorithm (may differ
            between bubble, insertion, and selection).

    Returns:
        ``ready`` when ``iter_position`` is the last pass, otherwise
        ``sorting``.
    """

    if iter_position == max_pass_index:
        current_status: str = SortingStatus.READY
    else:
        current_status = SortingStatus.SORTING

    return current_status
