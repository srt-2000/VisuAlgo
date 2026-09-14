"""Shared pytest fixtures for VisuAlgo tests."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.algorithms.insertion_sort import InsertionSorter


@pytest.fixture(scope="function")
def empty_list() -> list[int]:
    """Provide an empty list for edge-case tests.

    Returns:
        Empty list.
    """
    return []


@pytest.fixture(scope="class")
def binary_searcher() -> BinarySearch:
    """Give tests one shared ``BinarySearch`` instance.

    Returns:
        A binary search algorithm object.
    """
    return BinarySearch()


@pytest.fixture(scope="class")
def insertion_sorter() -> InsertionSorter:
    """Give tests one shared ``InsertionSorter`` instance.

    Returns:
        An insertion sort algorithm object.
    """
    return InsertionSorter()
