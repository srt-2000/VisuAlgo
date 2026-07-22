"""Helpers that build arrays for sorting demos and tests."""

from random import randint
from typing import Iterable


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
