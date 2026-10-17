"""Selection sort algorithm with step-by-step snapshots."""

from collections.abc import Iterator

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject
from backend.utils.sorting import get_current_sort_status


class SelectionSorter:
    """Sort a list copy by selection sort and expose step snapshots."""

    @staticmethod
    def iter_steps(array: list[int] | None) -> Iterator[BaseSortStepValueObject]:
        """Yield one snapshot after each minimum is swapped into place.

        The sort works on a copy, so the caller's list stays unchanged.
        An empty list, or ``None``, yields one ready snapshot and stops.
        A single-element list also yields one ready snapshot.

        Args:
            array: List of ints to sort. ``None`` is treated as empty.

        Yields:
            One snapshot per outer pass, or one ready snapshot for
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

        if n == 1:
            one_step_value: int = array_copy[0]

            yield BaseSortStepValueObject(
                index=0,
                value=one_step_value,
                before=(one_step_value,),
                result=(one_step_value,),
                status=SortingStatus.READY,
            )

        for i in range(n - 1):
            min_idx: int = i
            current_value: int = array_copy[i]
            before_state: tuple[int, ...] = tuple(array_copy.copy())

            for j in range(i + 1, n):
                if array_copy[j] < array_copy[min_idx]:
                    min_idx = j

            array_copy[i], array_copy[min_idx] = array_copy[min_idx], array_copy[i]

            current_result_state: tuple[int, ...] = tuple(array_copy)
            current_status: str = get_current_sort_status(
                iter_position=i,
                max_pass_index=(n - 2),
            )

            yield BaseSortStepValueObject(
                index=i,
                value=current_value,
                before=before_state,
                result=current_result_state,
                status=current_status,
            )
