"""Unit tests for sorting algorithms."""

import pytest

from algorithms.insertion_sort import InsertionSorter
from domains.sorting import InsertionSortStepValueObject, SortingStatus
from tests.atgorithms.insertion_sort.cases import (
    EXPECTED_DATA_SYNC_TEST,
    INPUT_DATA_SYNC_TEST,
    NOT_SORTED_ARRAYS,
)


class TestInsertionSort:
    """Check in-place insertion sort behavior."""

    @pytest.mark.parametrize("array", NOT_SORTED_ARRAYS)
    def test_insert_sort(
        self,
        get_insert_sorter: InsertionSorter,
        array: list[int],
    ) -> None:
        """``sort`` must sort the input list in place."""
        sorter = get_insert_sorter
        array_copy = array.copy()
        insertion_sort_result: list[int] = sorter.sort(array)
        expected: list[int] = sorted(array_copy)

        assert insertion_sort_result == expected
        assert array == expected
        assert insertion_sort_result is array

    def test_insert_sort_empty(
        self,
        get_insert_sorter: InsertionSorter,
        empty_list: list[int],
    ) -> None:
        """Empty list must stay unchanged."""
        sorter = get_insert_sorter
        array: list[int] = empty_list
        result: list[int] = sorter.sort(array)

        assert result == []
        assert result is array


class TestInsertionSortIterSteps:
    """Check step rules and one known golden sequence."""

    @pytest.mark.parametrize("array", NOT_SORTED_ARRAYS)
    def test_iter_steps_invariants(
        self,
        get_insert_sorter: InsertionSorter,
        array: list[int],
    ) -> None:
        """Each step must sort the current prefix and finish with a full sort."""
        sorter = get_insert_sorter
        array_copy = array.copy()
        sorting_steps: list[InsertionSortStepValueObject] = list(
            sorter.iter_steps(array)
        )
        expected_array_len: int = len(array_copy)
        expected_steps_quantity: int = len(array_copy) - 1
        expected_final_result: list[int] = sorted(array_copy)

        if expected_array_len <= 1:
            assert sorting_steps == []
            assert array == array_copy
            return

        steps_quantity: int = len(sorting_steps)
        assert steps_quantity == expected_steps_quantity

        for step in sorting_steps:
            assert 1 <= step.index < expected_array_len
            assert step.value == array_copy[step.index]
            assert isinstance(step.result, tuple)
            assert len(step.result) == expected_array_len

            sorted_part_end_index: int = step.index + 1
            sorted_array_part_left: list[int] = list(
                step.result[:sorted_part_end_index]
            )
            expected_sorted_part: list[int] = sorted(array_copy[:sorted_part_end_index])
            assert sorted_array_part_left == expected_sorted_part

            if step.index == expected_steps_quantity:
                expected_step_result: tuple[int, ...] = tuple(expected_final_result)
                assert step.status == SortingStatus.READY
                assert step.result == expected_step_result
            else:
                assert step.status == SortingStatus.SORTING

        assert array == expected_final_result

    def test_data_sync(
        self,
        get_insert_sorter: InsertionSorter,
    ) -> None:
        """Steps for a fixed case must match the golden expected list."""
        sorter = get_insert_sorter
        array: list[int] = INPUT_DATA_SYNC_TEST
        expected_result: list[int] = sorted(array)
        steps_container: list[InsertionSortStepValueObject] = list(
            sorter.iter_steps(array)
        )

        assert steps_container == EXPECTED_DATA_SYNC_TEST
        assert array == expected_result
