"""Insertion sort algorithm with step-by-step snapshots."""

from typing import Iterator

from backend.algorithms.interfaces import AlgorithmBase
from backend.domains.sorting import InsertionSortStepValueObject
from backend.utils.sorting import get_current_sorting_status


class InsertionSorter(AlgorithmBase):
    """Sort a list copy by insertion sort and expose step snapshots."""

    def iter_steps(
        self, array: list[int] | None
    ) -> Iterator[InsertionSortStepValueObject]:
        """Yield one snapshot after each insertion step.

        Args:
            array: List of ints to sort in place.

        Yields:
            One step snapshot after each key insertion.array
        """
        array_copy: list[int] = array.copy()

        if not array:
            current_status: str = get_current_sorting_status(
                iter_position=0,
                array_last_index=0,
            )

            yield InsertionSortStepValueObject(
                index=0,
                value=0,
                before=tuple(array_copy),
                result=tuple(array_copy),
                status=current_status,
            )

        for current_index in range(0, len(array_copy)):
            current_value: int = array_copy[current_index]
            check_index: int = current_index - 1
            before_state: list[int] = array_copy.copy()

            while check_index >= 0 and array_copy[check_index] > current_value:
                array_copy[check_index + 1] = array_copy[check_index]
                check_index -= 1

            array_copy[check_index + 1] = current_value
            current_status: str = get_current_sorting_status(
                iter_position=current_index,
                array_last_index=len(array_copy) - 1,
            )

            yield InsertionSortStepValueObject(
                index=current_index,
                value=current_value,
                before=tuple(before_state),
                result=tuple(array_copy),
                status=current_status,
            )
