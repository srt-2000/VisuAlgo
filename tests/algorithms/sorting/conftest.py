"""Pytest fixtures shared by sorting algorithm unit tests."""

import pytest

from tests.algorithms.sorting.cases import NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE


@pytest.fixture(scope="function", params=NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE)
def not_sorted_array_with_two_and_more_elements(request: pytest.FixtureRequest) -> list[int]:
    """Provide one unsorted list of length 2+ from fixture params.

    Args:
        request: Pytest request that holds the current parameter.

    Returns:
        The unsorted list for this test case.
    """
    param: list[int] = request.param

    return param
