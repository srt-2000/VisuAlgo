"""Unit tests for ``BinarySearch.search`` and ``BinarySearch.iter_steps``."""

import pytest

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStatus, BinarySearchStepValueObject
from tests.atgorithms.binary_search.cases import (
    BINARY_SEARCH_ITER_STEPS_INVARIANTS,
    EXPECTED_DATA_SYNC_TEST,
    INPUT_DATA_SYNC_TEST,
)


class TestBinarySearch:
    """Check that ``search`` finds indexes or returns ``None``."""

    def test_binary_search_with_filled_list(
        self,
        filled_list: list[int],
        get_binary_searcher: BinarySearch,
    ) -> None:
        """Present values get the right index; missing values get ``None``."""
        assert get_binary_searcher.search(filled_list, 3) == 2
        assert get_binary_searcher.search(filled_list, 9) == 8
        assert get_binary_searcher.search(filled_list, 9) != 9
        assert get_binary_searcher.search(filled_list, 10) is None

    def test_binary_search_with_empty_list(
        self,
        empty_list: list[int],
        get_binary_searcher: BinarySearch,
    ) -> None:
        """An empty list never has a match."""
        assert get_binary_searcher.search(empty_list, 0) is None
        assert get_binary_searcher.search(empty_list, 9) is None


class TestBinarySearchIterSteps:
    """Check step rules and one known golden sequence."""

    @pytest.mark.parametrize("test_case", BINARY_SEARCH_ITER_STEPS_INVARIANTS)
    def test_iter_steps_invariants(
        self,
        get_binary_searcher: BinarySearch,
        test_case: tuple[list[int], int],
    ) -> None:
        """Each step must stay inside bounds and use the right status."""
        array: list[int] = test_case[0]
        target: int = test_case[1]
        steps: list[BinarySearchStepValueObject] = list(
            get_binary_searcher.iter_steps(array, target)
        )

        if not array:
            assert steps == []
        else:
            for step in steps:
                assert (
                    0
                    <= step.left_index
                    <= step.mid_index
                    <= step.right_index
                    < len(array)
                )
                assert step.middle_value == array[step.mid_index]
                assert step.target == target

                if step.middle_value == target:
                    assert step.status == BinarySearchStatus.EQUAL
                elif step.middle_value > target:
                    assert step.status == BinarySearchStatus.GREATER
                else:
                    assert step.status == BinarySearchStatus.LESS

        if target in array:
            assert steps
            assert steps[-1].status == BinarySearchStatus.EQUAL
            assert array[steps[-1].mid_index] == target
        else:
            assert all(s.status != BinarySearchStatus.EQUAL for s in steps)

    def test_data_sync(self, get_binary_searcher: BinarySearch) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array, target = INPUT_DATA_SYNC_TEST
        assert (
            list(get_binary_searcher.iter_steps(array, target))
            == EXPECTED_DATA_SYNC_TEST
        )
