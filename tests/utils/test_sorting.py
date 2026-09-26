"""Unit tests for sorting utility helpers."""


import pytest

from tests.utils.cases import (
    RANDOM_NOT_ZERO_LIST_LIMITS,
    RANDOM_ZERO_ELEMENTS_LIST,
    INDEXES_AND_STATUS_RESULTS,
)
from backend.utils.sorting import get_not_sorted_random_list, get_current_sorting_status


class TestGetNotSortedRandomList:
    """Check length and value bounds of random list builder."""

    @pytest.mark.parametrize("test_limits", RANDOM_NOT_ZERO_LIST_LIMITS)
    def test_with_not_zero_limits(
        self,
        test_limits: tuple[int, int, int],
    ) -> None:
        """Non-zero length: size and min/max bounds must match the limits."""
        length_limit, min_value, max_value = test_limits
        random_list: list[int] = get_not_sorted_random_list(*test_limits)

        assert len(random_list) == length_limit
        assert min(random_list) >= min_value
        assert max(random_list) <= max_value

    @pytest.mark.parametrize("test_limits", RANDOM_ZERO_ELEMENTS_LIST)
    def test_with_zero_elements_quantity(
        self,
        test_limits: tuple[int, int, int],
        empty_list: list[int],
    ) -> None:
        """Zero length must return an empty list."""
        random_list: list[int] = get_not_sorted_random_list(*test_limits)

        assert len(random_list) == 0
        assert random_list == empty_list


class TestGetCurrentSortingStatus:
    @pytest.mark.parametrize("test_invariants", INDEXES_AND_STATUS_RESULTS)
    def test_all_invariants(self, test_invariants: tuple[int, int, str]) -> None:
        """Check all invariants of indexes and it results"""
        iter_position, array_last_index, expected_status = test_invariants
        status: str = get_current_sorting_status(
            iter_position=iter_position, array_last_index=array_last_index
        )

        assert status == expected_status
        assert isinstance(status, str)
