"""Pytest fixtures shared by algorithm unit tests."""

import pytest

from tests.algorithms.insertion_sort.cases import NOT_SORTED_ARRAYS


@pytest.fixture(scope="function")
def sorted_filled_list_with_nine_elements() -> list[int]:
    """Provide a small sorted list ``[1, 2, ..., 9]``.

    Returns:
        Non-empty sorted list of ints.
    """
    return list(range(1, 10))


@pytest.fixture(scope="function", params=NOT_SORTED_ARRAYS)
def array(request) -> tuple[list[int],...]:
    """Provide not sorted arrays for every testcase.

    Returns:
        tuple[list[int]]
    """

    return request.param
