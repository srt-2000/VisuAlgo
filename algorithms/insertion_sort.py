"""Insertion sort for lists of ints."""

from typing import Iterable


class InsertionSorter:
    """Sort a list by placing each next number into the sorted left part."""

    @staticmethod
    def sort(array: list[int]) -> list[int]:
        """Sort ``array`` from small to big, changing it in place.

        Args:
            array: List of ints (may be empty).

        Returns:
            The same list object, now sorted.
        """
        sorting_index_range: Iterable[int] = range(1, len(array))

        for current_index in sorting_index_range:
            current_value: int = array[current_index]
            check_index: int = current_index - 1

            while check_index >= 0 and array[check_index] > current_value:
                array[check_index + 1] = array[check_index]
                check_index -= 1

            array[check_index + 1] = current_value

        return array
