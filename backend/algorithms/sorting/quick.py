"""Quick sort algorithm with step-by-step partition snapshots."""

from collections.abc import Generator

from backend.algorithms.sorting.constants import RecursionTreeSide
from backend.domains.constants import SortingStatus
from backend.domains.sorting import QuickSortStepValueObject


class QuickSorter:
    """Sort a list copy by quicksort and expose partition step snapshots."""

    @staticmethod
    def iter_steps(
        array: list[int] | None,
        recursion_depth: int = 0,
        recursion_tree_side: str = RecursionTreeSide.ROOT,
    ) -> Generator[QuickSortStepValueObject, None, list[int]]:
        """Yield one snapshot after each partition, plus a final ready step.

        Works on a copy, so the caller's list stays unchanged. Empty /
        ``None`` at the root yields one ready snapshot and returns ``[]``.
        A single-element list at the root yields one ready snapshot and
        returns that one-element list. Nested calls yield only when the
        subarray has more than one element.

        Args:
            array: List of ints to sort. ``None`` is treated as empty.
            recursion_depth: Depth of the current recursive call (``0`` at root).
            recursion_tree_side: Branch label: ``root``, ``left``, or ``right``.

        Yields:
            One partition snapshot per recursive level that splits the array,
            plus a final ``ready`` snapshot when the root call finishes.

        Returns:
            The fully sorted list for this call's subarray.
        """
        if not array:
            if recursion_depth == 0:
                yield QuickSortStepValueObject(
                    depth=0,
                    side=recursion_tree_side,
                    pivot=0,
                    before=(),
                    result=([], [], []),
                    status=SortingStatus.READY,
                )
            return []

        array_copy: list[int] = array.copy()
        n: int = len(array_copy)

        if n == 1:
            one_step: list[int] = [array_copy[0]]
            if recursion_depth == 0:
                yield QuickSortStepValueObject(
                    depth=0,
                    side=recursion_tree_side,
                    pivot=one_step[0],
                    before=(one_step[0],),
                    result=([], one_step, []),
                    status=SortingStatus.READY,
                )
            return one_step

        pivot: int = array_copy[n // 2]
        left: list[int] = [v for v in array_copy if v < pivot]
        middle: list[int] = [v for v in array_copy if v == pivot]
        right: list[int] = [v for v in array_copy if v > pivot]
        next_depth: int = recursion_depth + 1

        yield QuickSortStepValueObject(
            depth=recursion_depth,
            side=recursion_tree_side,
            pivot=pivot,
            before=tuple(array_copy),
            result=(left, middle, right),
            status=SortingStatus.SORTING,
        )

        left_sorted: list[int] = yield from QuickSorter.iter_steps(
            array=left,
            recursion_depth=next_depth,
            recursion_tree_side=RecursionTreeSide.LEFT,
        )
        right_sorted: list[int] = yield from QuickSorter.iter_steps(
            array=right,
            recursion_depth=next_depth,
            recursion_tree_side=RecursionTreeSide.RIGHT,
        )

        assembled_array: list[int] = left_sorted + middle + right_sorted

        if recursion_depth == 0:
            yield QuickSortStepValueObject(
                depth=0,
                side=recursion_tree_side,
                pivot=pivot,
                before=tuple(array_copy),
                result=(left_sorted, middle, right_sorted),
                status=SortingStatus.READY,
            )

        return assembled_array
