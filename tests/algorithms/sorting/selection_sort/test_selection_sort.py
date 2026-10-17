"""Unit tests for ``SelectionSorter.iter_steps``."""

from backend.algorithms.sorting.selection import SelectionSorter
from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject
from tests.algorithms.sorting.selection_sort.cases import (
    EXPECTED_DATA_SYNC_TEST,
    INPUT_DATA_SYNC_TEST,
)


class TestSelectionSortIterSteps:
    """Check step rules and one known golden sequence."""

    def test_iter_steps_not_empty_invariants(
        self,
        selection_sorter: SelectionSorter,
        not_sorted_array_with_two_and_more_elements: list[int],
    ) -> None:
        """Each step must sort the current prefix and finish with a full sort."""
        array: list[int] = not_sorted_array_with_two_and_more_elements
        result_sorting_steps: list[BaseSortStepValueObject] = list(selection_sorter.iter_steps(array))
        result_array_after_sort: list[int] = list(result_sorting_steps[-1].result)
        expected_array_len: int = len(array)
        expected_steps_quantity: int = expected_array_len - 1
        expected_sorted_array: list[int] = sorted(array)
        result_steps_quantity: int = len(result_sorting_steps)

        assert result_steps_quantity == expected_steps_quantity

        for step in result_sorting_steps:
            current_index: int = step.index
            current_value: int = step.value
            final_step_index: int = len(result_sorting_steps) - 1
            step_before_state: tuple[int, ...] = step.before
            step_result_state: tuple[int, ...] = step.result
            min_value_after_current: int = min(step_before_state[current_index + 1 : :])
            min_value_before_index: int = step_before_state.index(min_value_after_current, current_index)

            assert 0 <= step.index < expected_array_len
            assert step.value == step.before[step.index]
            assert isinstance(step.result, tuple)
            assert len(step.result) == expected_array_len
            assert isinstance(step.before, tuple)
            assert len(step.before) == expected_array_len
            assert len(step.before) == len(step.result)

            if min_value_after_current < current_value:
                assert step_result_state[current_index] == min_value_after_current
                assert step_result_state[min_value_before_index] == current_value

            if current_index == final_step_index:
                expected_step_result: tuple[int, ...] = tuple(expected_sorted_array)

                assert step.status == SortingStatus.READY
                assert step.result == expected_step_result
            else:
                assert step.status == SortingStatus.SORTING

        assert result_array_after_sort == expected_sorted_array

    def test_iter_steps_one_element(
        self,
        selection_sorter: SelectionSorter,
        one_element_array: list[int],
    ) -> None:
        """A single-element list yields one ready snapshot and stays unchanged."""
        sorting_steps: list[BaseSortStepValueObject] = list(selection_sorter.iter_steps(one_element_array))
        steps_quantity: int = len(sorting_steps)
        expected_array_len: int = 1
        expected_steps_quantity: int = 1
        expected_sorted_array: list[int] = sorted(one_element_array)

        assert steps_quantity == expected_steps_quantity

        only_step: BaseSortStepValueObject = sorting_steps[0]

        assert only_step.index == 0
        assert only_step.value == one_element_array[0]
        assert isinstance(only_step.result, tuple)
        assert len(only_step.result) == expected_array_len
        assert isinstance(only_step.before, tuple)
        assert len(only_step.before) == expected_array_len
        assert only_step.status == SortingStatus.READY
        assert only_step.result == tuple(expected_sorted_array)

    def test_selection_sort_empty_invariant(
        self,
        selection_sorter: SelectionSorter,
        empty_list: list[int],
    ) -> None:
        """An empty list yields one ready snapshot and does not invent numbers."""
        sorting_steps: list[BaseSortStepValueObject] = list(selection_sorter.iter_steps(empty_list))
        expected_array_len: int = 0
        expected_steps_quantity: int = 1
        expected_sorted_array: list[int] = []

        steps_quantity: int = len(sorting_steps)
        assert steps_quantity == expected_steps_quantity

        step: BaseSortStepValueObject = sorting_steps[0]
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
        selection_sorter: SelectionSorter,
    ) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array: list[int] = INPUT_DATA_SYNC_TEST
        expected_sorted_array: list[int] = sorted(array)
        expected_steps: list[BaseSortStepValueObject] = EXPECTED_DATA_SYNC_TEST
        steps_container: list[BaseSortStepValueObject] = list(selection_sorter.iter_steps(array))
        sorted_array: list[int] = list(steps_container[-1].result)

        assert steps_container == expected_steps
        assert sorted_array == expected_sorted_array
