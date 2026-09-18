"""Helpers that build arrays for sorting demos and tests."""

from random import randint
from typing import Iterable, Literal

from backend.utils.constants import SortingStatus


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

def get_current_sorting_status(iter_position: int, array_last_index: int) -> str:
    """Get the sorting status of the current iteration.

    Args:
        iter_position: int Current iteration position index.
        array_last_index: int Last index of iterating array.

    Returns:
        A str constant with status name.
        """
    if iter_position == array_last_index:
        current_status: str = SortingStatus.READY
    else:
        current_status: str = SortingStatus.SORTING

    return current_status