"""Unit tests for ``BubbleSorter.iter_steps``."""

from backend.algorithms.bubble_sort import BubbleSorter
from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject
from tests.algorithms.bubble_sort.cases import BUBBLE_SORT_EXPECTED_DATA_SYNC_TEST, BUBLE_SORT_DATA_SYNC_TEST


class TestBubbleSortIterSteps:
    """Check step rules and one known golden sequence."""

    def test_iter_steps_not_empty_invariants(
        self,
        bubble_sorter: BubbleSorter,
        array_with_two_and_more_elements: list[int],
    ) -> None:
        """Each step must sort the current prefix and finish with a full sort."""
        array: list[int] = array_with_two_and_more_elements
        result_sorting_steps: list[BaseSortStepValueObject] = list(bubble_sorter.iter_steps(array))
        result_array_after_sort: list[int] = list(result_sorting_steps[-1].result)
        expected_array_len: int = len(array)
        expected_steps_quantity: int = expected_array_len * (expected_array_len - 1) // 2
        expected_sorted_array: list[int] = sorted(array)
        result_steps_quantity: int = len(result_sorting_steps)

        assert result_steps_quantity <= expected_steps_quantity

        for current_step_index, step in enumerate(result_sorting_steps):
            current_element_index: int = step.index
            current_value: int = step.value
            final_step_index: int = len(result_sorting_steps) - 1

            assert 0 <= step.index < expected_array_len
            assert step.value == step.before[step.index]
            assert isinstance(step.result, tuple)
            assert len(step.result) == expected_array_len
            assert isinstance(step.before, tuple)
            assert len(step.before) == expected_array_len
            assert len(step.before) == len(step.result)

            if (
                current_element_index < (len(step.result) - 1)
                and step.before[current_element_index] > step.before[current_element_index + 1]
            ):
                next_element: int = step.result[current_element_index + 1]
                assert next_element == current_value

            if current_step_index == final_step_index:
                expected_step_result: tuple[int, ...] = tuple(expected_sorted_array)

                assert step.status == SortingStatus.READY
                assert step.result == expected_step_result
            else:
                assert step.status == SortingStatus.SORTING

        assert result_array_after_sort == expected_sorted_array

    def test_iter_steps_one_element(
        self,
        bubble_sorter: BubbleSorter,
        one_element_array: list[int],
    ) -> None:
        """A single-element list yields one ready snapshot and stays unchanged."""
        sorting_steps: list[BaseSortStepValueObject] = list(bubble_sorter.iter_steps(one_element_array))
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

    def test_bubble_sort_empty_invariant(
        self,
        bubble_sorter: BubbleSorter,
        empty_list: list[int],
    ) -> None:
        """An empty list yields one ready snapshot and does not invent numbers."""
        sorting_steps: list[BaseSortStepValueObject] = list(bubble_sorter.iter_steps(empty_list))
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
        bubble_sorter: BubbleSorter,
    ) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array: list[int] = BUBLE_SORT_DATA_SYNC_TEST
        expected_sorted_array: list[int] = sorted(array)
        expected_steps: list[BaseSortStepValueObject] = BUBBLE_SORT_EXPECTED_DATA_SYNC_TEST
        steps_container: list[BaseSortStepValueObject] = list(bubble_sorter.iter_steps(array))
        sorted_array: list[int] = list(steps_container[-1].result)

        assert steps_container == expected_steps
        assert sorted_array == expected_sorted_array
