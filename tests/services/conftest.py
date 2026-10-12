"""Pytest fixtures shared by service-layer unit tests."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.algorithms.bubble_sort import BubbleSorter
from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.binary_search import BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus, SortingStatus
from backend.domains.sorting import BaseSortStepValueObject
from backend.services.binary_search import BinarySearchProcessDataLogger
from backend.services.bubble_sort import BubbleSortProcessDataLogger
from backend.services.constants import Fields
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
    """Build a fresh insertion-sort process logger for one test.

    Args:
        insertion_sorter: Shared insertion sort engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return InsertionSortProcessDataLogger(insertion_sorter)


@pytest.fixture(scope="function")
def bubble_sort_process_data_logger(
    bubble_sorter: BubbleSorter,
) -> BubbleSortProcessDataLogger:
    """Build a fresh bubble-sort process logger for one test.

    Args:
        bubble_sorter: Shared bubble sort engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return BubbleSortProcessDataLogger(bubble_sorter)


@pytest.fixture(scope="function")
def expected_log_fields() -> tuple[str, ...]:
    """Field names that every sort process log must fill.

    Returns:
        Tuple of column names on ``BaseSortAlgorithmLogDTO``.
    """
    return (
        Fields.INDEX,
        Fields.VALUE,
        Fields.BEFORE,
        Fields.RESULT,
        Fields.SORT_STATUS,
    )


@pytest.fixture(scope="function")
def binary_search_test_step_data() -> BinarySearchStepValueObject:
    """Provide one sample binary-search step for logger tests.

    Returns:
        Frozen step with fixed indexes and ``LESS`` status.
    """
    step_data: BinarySearchStepValueObject = BinarySearchStepValueObject(
        left_index=2,
        left_value=26,
        right_index=8,
        right_value=79,
        mid_index=5,
        middle_value=58,
        status=BinarySearchStatus.LESS,
        target=60,
    )

    return step_data


@pytest.fixture(scope="function")
def insertion_sort_test_step_data() -> BaseSortStepValueObject:
    """Provide one sample insertion-sort step for logger tests.

    Returns:
        Frozen step with fixed index, value, and ``SORTING`` status.
    """
    step_data: BaseSortStepValueObject = BaseSortStepValueObject(
        index=2,
        value=3,
        before=(2, 38, 3),
        result=(2, 3, 38),
        status=SortingStatus.SORTING,
    )

    return step_data


@pytest.fixture(scope="function")
def bubble_sort_test_step_data() -> BaseSortStepValueObject:
    """Provide one sample bubble-sort step for logger tests.

    Returns:
        Frozen step with fixed index, value, and ``SORTING`` status.
    """
    step_data: BaseSortStepValueObject = BaseSortStepValueObject(
        index=1,
        value=38,
        before=(2, 38, 3, 33),
        result=(2, 3, 38, 33),
        status=SortingStatus.SORTING,
    )

    return step_data
