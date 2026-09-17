"""Pytest fixtures shared by service-layer unit tests."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from backend.domains.sorting import InsertionSortStepValueObject
from backend.utils.constants import SortingStatus
from backend.services.binary_search import BinarySearchProcessDataLogger
from backend.services.insertion_sort import InsertionSortProcessDataLogger


@pytest.fixture(scope="function")
def binary_search_process_data_logger(
    binary_searcher: BinarySearch,
) -> BinarySearchProcessDataLogger:
    """Build a fresh process logger for one test.

    Args:
        binary_searcher: Shared binary search engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return BinarySearchProcessDataLogger(binary_searcher)


@pytest.fixture(scope="function")
def insertion_sort_process_data_logger(
    insertion_sorter: InsertionSorter,
) -> InsertionSortProcessDataLogger:
    """Build a fresh sort process logger for one test.

    Args:
        insertion_sorter: Shared insertion sort engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return InsertionSortProcessDataLogger(insertion_sorter)


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


@pytest.fixture(scope="function")
def insertion_sort_test_step_data() -> InsertionSortStepValueObject:
    """Provide one sample insertion-sort step for logger tests.

    Returns:
        Frozen step with fixed index, value, and ``SORTING`` status.
    """
    step_data: InsertionSortStepValueObject = InsertionSortStepValueObject(
        index=2,
        value=3,
        before=(2, 38, 3),
        result=(2, 3, 38),
        status=SortingStatus.SORTING,
    )

    return step_data
