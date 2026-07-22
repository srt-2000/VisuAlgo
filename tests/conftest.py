"""Shared pytest fixtures for VisuAlgo tests."""

import pytest

from algorithms.binary_search import BinarySearch
from algorithms.insertion_sort import InsertionSorter
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.binary_search import BinarySearchProcessDataLogger


@pytest.fixture(scope="class")
def get_binary_searcher() -> BinarySearch:
    """Give tests one shared ``BinarySearch`` instance.

    Returns:
        A binary search algorithm object.
    """
    return BinarySearch()


@pytest.fixture(scope="class")
def get_insert_sorter() -> InsertionSorter:
    """Give tests one shared ``InsertionSorter`` instance.

    Returns:
        An insertion sort algorithm object.
    """
    return InsertionSorter()


@pytest.fixture(scope="function")
def get_binary_search_process_data_logger(
    get_binary_searcher: BinarySearch,
) -> BinarySearchProcessDataLogger:
    """Build a fresh process logger for one test.

    Args:
        get_binary_searcher: Shared binary search engine fixture.

    Returns:
        Logger with an empty ``search_log``.
    """
    return BinarySearchProcessDataLogger(get_binary_searcher)


@pytest.fixture(scope="function")
def filled_list() -> list[int]:
    """Provide a small sorted list ``[1, 2, ..., 9]``.

    Returns:
        Non-empty sorted list of ints.
    """
    return list(range(1, 10))


@pytest.fixture(scope="function")
def empty_list() -> list[int]:
    """Provide an empty list for edge-case tests.

    Returns:
        Empty list.
    """
    return []


@pytest.fixture(scope="function")
def binary_search_test_step_data() -> BinarySearchStepValueObject:
    """Provide one sample binary-search step for logger tests.

    Returns:
        Frozen step with fixed indexes and ``GREATER`` status.
    """
    step_data: BinarySearchStepValueObject = BinarySearchStepValueObject(
        left_index=2,
        right_index=8,
        mid_index=5,
        middle_value=58,
        status=BinarySearchStatus.GREATER,
        target=60,
    )

    return step_data
