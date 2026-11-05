"""Unit tests for ``QuickSorter.iter_steps``."""

from collections.abc import Generator

from backend.algorithms.sorting.constants import RecursionTreeSide
from backend.algorithms.sorting.quick import QuickSorter
from backend.domains.constants import SortingStatus
from backend.domains.sorting import QuickSortStepValueObject
from tests.algorithms.sorting.quick.cases import (
    ALREADY_SORTED_ARRAY,
    EXPECTED_DATA_SYNC_TEST,
    INPUT_DATA_SYNC_TEST,
    TWO_ELEMENT_ARRAY,
)


class TestQuickSortIterSteps:
    """Check step rules and one known golden sequence."""

    def _flatten_partition(self, result: tuple[list[int], ...]) -> list[int]:
        """Flatten a left/middle/right partition into one list.

        Args:
            result: Partition triple from a quick-sort step.

        Returns:
            Values in left-to-right order.
        """
        return [element for part in result for element in part]

    def _drain_steps(
        self,
        generator: Generator[QuickSortStepValueObject, None, list[int]],
    ) -> tuple[list[QuickSortStepValueObject], list[int]]:
        """Collect yielded steps and the generator return value.

        Args:
            generator: ``QuickSorter.iter_steps`` generator.

        Returns:
            Yielded snapshots and the final sorted list from ``return``.
        """
        steps: list[QuickSortStepValueObject] = []
        try:
            while True:
                steps.append(next(generator))
        except StopIteration as stop:
            sorted_array: list[int] = stop.value if stop.value is not None else []
            return steps, sorted_array

    def test_iter_steps_not_empty_invariants(
        self,
        quick_sorter: QuickSorter,
        not_sorted_array_with_two_and_more_elements: list[int],
    ) -> None:
        """Partition steps must keep a permutation and finish fully sorted."""
        array: list[int] = not_sorted_array_with_two_and_more_elements
        array_copy: list[int] = array.copy()
        expected_sorted_array: list[int] = sorted(array)
        steps: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(array))

        assert array == array_copy
        assert steps
        assert steps[0].side == RecursionTreeSide.ROOT
        assert steps[0].depth == 0
        assert steps[-1].status == SortingStatus.READY
        assert all(step.status == SortingStatus.SORTING for step in steps[:-1])

        for step in steps:
            flat: list[int] = self._flatten_partition(step.result)
            left, middle, right = step.result

            assert step.pivot == step.before[len(step.before) // 2]
            assert sorted(step.before) == sorted(flat)
            assert step.side in {RecursionTreeSide.ROOT, RecursionTreeSide.LEFT, RecursionTreeSide.RIGHT}
            assert step.depth >= 0
            assert (step.side == RecursionTreeSide.ROOT) == (step.depth == 0)
            assert all(value < step.pivot for value in left)
            assert all(value == step.pivot for value in middle)
            assert all(value > step.pivot for value in right)
            assert middle

        assert self._flatten_partition(steps[-1].result) == expected_sorted_array

    def test_iter_steps_two_elements(
        self,
        quick_sorter: QuickSorter,
    ) -> None:
        """A two-element list yields a valid partition tree and sorted result."""
        array: list[int] = TWO_ELEMENT_ARRAY.copy()
        array_copy: list[int] = array.copy()
        steps: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(array))

        assert array == array_copy
        assert steps
        assert steps[0].status == SortingStatus.SORTING
        assert steps[-1].status == SortingStatus.READY
        assert self._flatten_partition(steps[-1].result) == sorted(array_copy)

    def test_iter_steps_already_sorted(
        self,
        quick_sorter: QuickSorter,
    ) -> None:
        """An already sorted list still yields partitions and a ready result."""
        array: list[int] = ALREADY_SORTED_ARRAY.copy()
        steps: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(array))

        assert steps
        assert steps[-1].status == SortingStatus.READY
        assert self._flatten_partition(steps[-1].result) == ALREADY_SORTED_ARRAY

    def test_iter_steps_one_element(
        self,
        quick_sorter: QuickSorter,
        one_element_array: list[int],
    ) -> None:
        """A single-element list yields one ready snapshot and stays unchanged."""
        array_copy: list[int] = one_element_array.copy()
        sorting_steps: list[QuickSortStepValueObject] = list(
            quick_sorter.iter_steps(one_element_array),
        )
        only_step: QuickSortStepValueObject = sorting_steps[0]
        flat: list[int] = self._flatten_partition(only_step.result)

        assert one_element_array == array_copy
        assert len(sorting_steps) == 1
        assert only_step.depth == 0
        assert only_step.side == RecursionTreeSide.ROOT
        assert only_step.pivot == one_element_array[0]
        assert only_step.before == (one_element_array[0],)
        assert flat == array_copy
        assert only_step.status == SortingStatus.READY

    def test_quick_sort_empty_invariant(
        self,
        quick_sorter: QuickSorter,
        empty_list: list[int],
    ) -> None:
        """An empty list yields one ready snapshot and does not invent numbers."""
        sorting_steps: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(empty_list))
        step: QuickSortStepValueObject = sorting_steps[0]
        flat: list[int] = self._flatten_partition(step.result)

        assert len(sorting_steps) == 1
        assert step.depth == 0
        assert step.side == RecursionTreeSide.ROOT
        assert step.pivot == 0
        assert step.before == ()
        assert step.result == ([], [], [])
        assert flat == []
        assert step.status == SortingStatus.READY

    def test_iter_steps_none_like_empty(
        self,
        quick_sorter: QuickSorter,
    ) -> None:
        """``None`` is treated as an empty root input."""
        sorting_steps: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(None))
        step: QuickSortStepValueObject = sorting_steps[0]

        assert len(sorting_steps) == 1
        assert step.status == SortingStatus.READY
        assert step.before == ()
        assert step.result == ([], [], [])
        assert self._flatten_partition(step.result) == []

    def test_iter_steps_return_value(
        self,
        quick_sorter: QuickSorter,
    ) -> None:
        """Generator return value is the fully sorted list."""
        array: list[int] = [3, 1, 2]
        steps, returned = self._drain_steps(quick_sorter.iter_steps(array))

        assert steps
        assert steps[-1].status == SortingStatus.READY
        assert returned == [1, 2, 3]
        assert returned == self._flatten_partition(steps[-1].result)

    def test_data_sync(
        self,
        quick_sorter: QuickSorter,
    ) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array: list[int] = INPUT_DATA_SYNC_TEST
        expected_sorted_array: list[int] = sorted(array)
        expected_steps: list[QuickSortStepValueObject] = EXPECTED_DATA_SYNC_TEST
        steps_container: list[QuickSortStepValueObject] = list(quick_sorter.iter_steps(array))
        result_array_after_sort: list[int] = self._flatten_partition(steps_container[-1].result)

        assert steps_container == expected_steps
        assert result_array_after_sort == expected_sorted_array
