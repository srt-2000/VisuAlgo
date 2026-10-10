"""Pytest fixtures shared by algorithm unit tests."""

import pytest

from tests.algorithms.bubble_sort.cases import NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE
from tests.algorithms.insertion_sort.cases import NOT_SORTED_ARRAYS


@pytest.fixture(scope="function")
def sorted_filled_list_with_nine_elements() -> list[int]:
    """Provide a small sorted list ``[1, 2, ..., 9]``.

    Returns:
        Non-empty sorted list of ints.
    """
    return list(range(1, 10))


@pytest.fixture(scope="function", params=NOT_SORTED_ARRAYS)
def array(request: pytest.FixtureRequest) -> list[int]:
    """Provide one unsorted list from ``NOT_SORTED_ARRAYS``.

    Args:
        request: Pytest request that holds the current parameter.

    Returns:
        The unsorted list for this test case.
    """
    param: list[int] = request.param

    return param


@pytest.fixture(scope="function", params=NOT_SORTED_ARRAYS_WITH_TWO_ELEMENTS_AND_MORE)
def array_with_two_and_more_elements(request: pytest.FixtureRequest) -> list[int]:
    """Provide one unsorted list of length 2+ from fixture params.

    Args:
        request: Pytest request that holds the current parameter.

    Returns:
        The unsorted list for this test case.
    """
    param: list[int] = request.param

    return param
