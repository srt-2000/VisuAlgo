"""Shared pytest fixtures for algorithm unit tests."""

import pytest

from algorithms.binary_search import BinarySearch
from algorithms.insertion_sort import InsertionSorter


@pytest.fixture(scope="class")
def binary_search() -> BinarySearch:
    """Provide a reusable ``BinarySearch`` instance for a test class.

    Returns:
        Stateless binary search algorithm instance.
    """
    return BinarySearch()


@pytest.fixture(scope="class")
def insert_sorter() -> InsertionSorter:
    """Provide a reusable ``InsertionSorter`` instance for a test class.

    Returns:
        Insertion sort algorithm instance.
    """
    return InsertionSorter()


@pytest.fixture(scope="function")
def filled_list() -> list[int]:
    """Provide a non-empty sorted list of integers for search scenarios.

    Returns:
        Sorted list ``[1, 2, ..., 9]``.
    """
    return list(range(1, 10))


@pytest.fixture(scope="function")
def empty_list() -> list[int]:
    """Provide an empty list for edge-case search and sort scenarios.

    Returns:
        Empty list.
    """
    return []
