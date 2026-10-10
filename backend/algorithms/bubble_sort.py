"""Bubble sort algorithm with step-by-step snapshots."""

from collections.abc import Iterator

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject
from backend.utils.sorting import get_current_sort_status


class BubbleSorter:
    """Sort a list copy by bubble sort and expose step snapshots."""

    @staticmethod
    def iter_steps(array: list[int] | None) -> Iterator[BaseSortStepValueObject]:
        """Yield one snapshot after each adjacent comparison.

        The sort works on a copy, so the caller's list stays unchanged.
        An empty list, or ``None``, yields one ready snapshot and stops.
        A single-element list also yields one ready snapshot.

        Args:
            array: List of ints to sort. ``None`` is treated as empty.

        Yields:
            One snapshot per comparison, or one ready snapshot for
            empty / singleton input.
        """
        if not array:
            yield BaseSortStepValueObject(
                index=0,
                value=0,
                before=(),
                result=(),
                status=SortingStatus.READY,
            )
            return

        array_copy: list[int] = array.copy()
        n: int = len(array_copy)
        final_pass_index: int = n - 2

        if n == 1:
            one_step_value: int = array_copy[0]

            yield BaseSortStepValueObject(
                index=0,
                value=one_step_value,
                before=(one_step_value,),
                result=(one_step_value,),
                status=SortingStatus.READY,
            )
            return

        for pass_index in range(n - 1):
            for current_index in range(n - 1 - pass_index):
                current_value: int = array_copy[current_index]
                before_state: tuple[int, ...] = tuple(array_copy)

                if array_copy[current_index] > array_copy[current_index + 1]:
                    (
                        array_copy[current_index],
                        array_copy[current_index + 1],
                    ) = (
                        array_copy[current_index + 1],
                        array_copy[current_index],
                    )

                current_result_state: tuple[int, ...] = tuple(array_copy)
                current_status: str = get_current_sort_status(
                    iter_position=pass_index,
                    array_last_index=final_pass_index,
                )

                yield BaseSortStepValueObject(
                    index=current_index,
                    value=current_value,
                    before=before_state,
                    result=current_result_state,
                    status=current_status,
                )
