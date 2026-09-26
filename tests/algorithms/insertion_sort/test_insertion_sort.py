"""Unit tests for ``InsertionSorter.sort`` and ``InsertionSorter.iter_steps``."""

from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.sorting import InsertionSortStepValueObject
from backend.domains.constants import SortingStatus
from tests.algorithms.insertion_sort.cases import (
    INSERTION_SORT_EXPECTED_DATA_SYNC_TEST,
    INSERTION_SORT_DATA_SYNC_TEST,
)


class TestInsertionSort:
    """Check in-place insertion sort behavior."""

    def test_insert_sort(
        self,
        insertion_sorter: InsertionSorter,
        array: list[int],
    ) -> None:
        """``sort`` must sort the input list in place."""
        array_copy = array.copy()
        sort_result: list[int] = insertion_sorter.sort(array)
        expected: list[int] = sorted(array_copy)

        assert sort_result == expected
        assert array == expected
        assert sort_result is array

    def test_insert_sort_empty(
        self,
        insertion_sorter: InsertionSorter,
        empty_list: list[int],
    ) -> None:
        """Empty list must stay unchanged."""
        expected_array: list[int] = empty_list.copy()
        sort_result: list[int] = insertion_sorter.sort(empty_list)

        assert sort_result == expected_array


class TestInsertionSortIterSteps:
    """Check step rules and one known golden sequence."""

    def test_iter_steps_not_empty_invariants(
        self,
        insertion_sorter: InsertionSorter,
        array: list[int],
    ) -> None:
        """Each step must sort the current prefix and finish with a full sort."""
        array_copy = array.copy()
        sorting_steps: list[InsertionSortStepValueObject] = list(
            insertion_sorter.iter_steps(array)
        )
        expected_array_len: int = len(array_copy)
        expected_steps_quantity: int = expected_array_len
        expected_sorted_array: list[int] = sorted(array_copy)

        steps_quantity: int = len(sorting_steps)
        assert steps_quantity == expected_steps_quantity

        for step in sorting_steps:
            assert 0 <= step.index < expected_array_len
            assert step.value == array_copy[step.index]
            assert isinstance(step.result, tuple)
            assert len(step.result) == expected_array_len
            assert isinstance(step.before, tuple)
            assert len(step.before) == expected_array_len

            sorted_part_end_index: int = step.index + 1
            sorted_array_part_left: list[int] = list(
                step.result[:sorted_part_end_index]
            )
            expected_sorted_part: list[int] = sorted(array_copy[:sorted_part_end_index])
            assert sorted_array_part_left == expected_sorted_part

            if step.index == expected_steps_quantity - 1:
                expected_step_result: tuple[int, ...] = tuple(expected_sorted_array)
                assert step.status == SortingStatus.READY
                assert step.result == expected_step_result
            else:
                assert step.status == SortingStatus.SORTING

        assert array == expected_sorted_array

    def test_insertion_sort_empty_invariant(
        self,
        insertion_sorter: InsertionSorter,
        empty_list: list[int],
    ) -> None:
        sorting_steps: list[InsertionSortStepValueObject] = list(
            insertion_sorter.iter_steps(empty_list)
        )
        expected_array_len: int = 0
        expected_steps_quantity: int = 1
        expected_sorted_array: list[int] = []

        steps_quantity: int = len(sorting_steps)
        assert steps_quantity == expected_steps_quantity

        step: InsertionSortStepValueObject = sorting_steps[0]
        assert step.index == 0
        assert step.value == 0
        assert isinstance(step.result, tuple)
        assert len(step.result) == expected_array_len
        assert isinstance(step.before, tuple)
        assert len(step.before) == expected_array_len
        assert step.status == SortingStatus.READY
        assert empty_list == expected_sorted_array

    def test_data_sync(
        self,
        insertion_sorter: InsertionSorter,
    ) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array: list[int] = INSERTION_SORT_DATA_SYNC_TEST
        expected_sorted_array: list[int] = sorted(array)
        expected_steps: list[InsertionSortStepValueObject] = (
            INSERTION_SORT_EXPECTED_DATA_SYNC_TEST
        )
        steps_container: list[InsertionSortStepValueObject] = list(
            insertion_sorter.iter_steps(array)
        )

        assert steps_container == expected_steps
        assert array == expected_sorted_array
