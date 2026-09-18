"""Insertion sort algorithm with step-by-step snapshots."""

from typing import Iterator

from backend.algorithms.interfaces import AlgorithmBase
from backend.domains.sorting import InsertionSortStepValueObject
from backend.utils.sorting import get_current_sorting_status


class InsertionSorter(AlgorithmBase):
    """Sort a list in place by insertion sort and expose step snapshots."""

    def sort(self, array: list[int]) -> list[int]:
        """Sort ``array`` in place and return the same list object.

        Args:
            array: List of ints to sort.

        Returns:
            The same list object after in-place sorting.
        """
        for _ in self.iter_steps(array):
            pass
        return array

    @staticmethod
    def iter_steps(array: list[int] | None) -> Iterator[InsertionSortStepValueObject]:
        """Yield one snapshot after each insertion step.

        Args:
            array: List of ints to sort in place.

        Yields:
            One step snapshot after each key insertion.
        """
        if not array:
            current_status: str = get_current_sorting_status(
                iter_position=0,
                array_last_index=0,
            )

            yield InsertionSortStepValueObject(
                index=0,
                value=0,
                before=tuple(array),
                result=tuple(array),
                status=current_status,
            )

        for current_index in range(0, len(array)):
            current_value: int = array[current_index]
            check_index: int = current_index - 1
            before_state: list[int] = array.copy()

            while check_index >= 0 and array[check_index] > current_value:
                array[check_index + 1] = array[check_index]
                check_index -= 1

            array[check_index + 1] = current_value
            current_status: str = get_current_sorting_status(
                iter_position=current_index,
                array_last_index=len(array) - 1,
            )

            yield InsertionSortStepValueObject(
                index=current_index,
                value=current_value,
                before=tuple(before_state),
                result=tuple(array),
                status=current_status,
            )
