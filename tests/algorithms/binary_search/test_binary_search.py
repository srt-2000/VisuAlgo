"""Unit tests for ``BinarySearch.search`` and ``BinarySearch.iter_steps``."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.domains.binary_search import BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus
from tests.algorithms.binary_search.cases import (
    BINARY_SEARCH_ITER_STEPS_INVARIANTS,
    BINARY_SEARCH_EXPECTED_DATA_SYNC_TEST,
    BINARY_SEARCH_DATA_SYNC_TEST,
)


class TestBinarySearchIterSteps:
    """Check step rules and one known golden sequence."""

    @pytest.mark.parametrize("test_case", BINARY_SEARCH_ITER_STEPS_INVARIANTS)
    def test_iter_steps_invariants(
        self,
        binary_searcher: BinarySearch,
        test_case: tuple[list[int], int],
        empty_list: list[int],
    ) -> None:
        """Each step must stay inside bounds and use the right status."""
        array, target = test_case
        steps: list[BinarySearchStepValueObject] = list(
            binary_searcher.iter_steps(array, target)
        )

        if not array:
            assert steps == empty_list
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

            final_status: str = steps[-1].status
            founded_index: int = steps[-1].mid_index
            founded_value: int = array[founded_index]
            assert final_status == BinarySearchStatus.EQUAL
            assert founded_value == target
        else:
            assert all(step.status != BinarySearchStatus.EQUAL for step in steps)

    def test_data_sync(self, binary_searcher: BinarySearch) -> None:
        """Steps for a fixed case must match the golden expected list."""
        array, target = BINARY_SEARCH_DATA_SYNC_TEST
        expected_steps: list[BinarySearchStepValueObject] = (
            BINARY_SEARCH_EXPECTED_DATA_SYNC_TEST
        )
        steps_container: list[BinarySearchStepValueObject] = list(
            binary_searcher.iter_steps(array, target)
        )

        assert steps_container == expected_steps
