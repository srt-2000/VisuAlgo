"""Insertion sort algorithm for integer arrays."""

from typing import Iterable


class InsertionSorter:
    """In-place insertion sort for lists of integers."""

    @staticmethod
    def sort(array: list[int]) -> list[int]:
        """Sort ``array`` ascending using insertion sort.

        Mutates ``array`` in place and returns the same list object.

        Args:
            array: List of integers to sort. May be empty.

        Returns:
            The sorted ``array`` (same object, mutated in place).
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
