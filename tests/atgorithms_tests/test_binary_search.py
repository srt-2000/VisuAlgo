"""Unit tests for ``BinarySearch.search`` and ``BinarySearch.iter_steps``."""

import pytest

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStatus, BinarySearchStepValueObject
from tests.atgorithms_tests.testcases import (
    BINARY_SEARCH_ITER_STEPS_INVARIANTS,
    EXPECTED_DATA_SYNC_TEST,
    INPUT_DATA_SYNC_TEST,
)


class TestBinarySearch:
    """Validate index lookup behavior of ``BinarySearch.search``."""

    def test_binary_search_with_filled_list(
        self,
        filled_list: list[int],
        binary_search: BinarySearch,
    ) -> None:
        """Return correct indices for present and missing values."""
        assert binary_search.search(filled_list, 3) == 2
        assert binary_search.search(filled_list, 9) == 8
        assert binary_search.search(filled_list, 9) != 9
        assert binary_search.search(filled_list, 10) is None

    def test_binary_search_with_empty_list(
        self,
        empty_list: list[int],
        binary_search: BinarySearch,
    ) -> None:
        """Return ``None`` when searching an empty array."""
        assert binary_search.search(empty_list, 0) is None
        assert binary_search.search(empty_list, 9) is None


class TestBinarySearchIterSteps:
    """Validate step iterator invariants and golden step sequences."""

    @pytest.mark.parametrize("test_case", BINARY_SEARCH_ITER_STEPS_INVARIANTS)
    def test_iter_steps_invariants(
        self,
        binary_search: BinarySearch,
        test_case: tuple[list[int], int],
    ) -> None:
        """Check per-step and terminal invariants for representative cases.

        Asserts empty yield for empty arrays, bounds/status consistency for
        each step, and correct EQUAL / non-EQUAL termination.
        """
        array: list[int] = test_case[0]
        target: int = test_case[1]
        steps: list[BinarySearchStepValueObject] = list(
            binary_search.iter_steps(array, target)
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

    def test_data_sync(self, binary_search: BinarySearch) -> None:
        """Match the golden step sequence for a fixed array and target."""
        array, target = INPUT_DATA_SYNC_TEST
        assert list(binary_search.iter_steps(array, target)) == EXPECTED_DATA_SYNC_TEST
