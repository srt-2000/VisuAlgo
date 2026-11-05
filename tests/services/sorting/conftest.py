"""Pytest fixtures for sorting process-logger unit tests."""

import pytest

from backend.algorithms.sorting.bubble import BubbleSorter
from backend.algorithms.sorting.constants import RecursionTreeSide
from backend.algorithms.sorting.insertion import InsertionSorter
from backend.algorithms.sorting.quick import QuickSorter
from backend.algorithms.sorting.selection import SelectionSorter
from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortStepValueObject, QuickSortStepValueObject
from backend.services.constants import Fields
from backend.services.sorting.bubble import BubbleSortProcessDataLogger
from backend.services.sorting.insertion import InsertionSortProcessDataLogger
from backend.services.sorting.quick import QuickSortProcessDataLogger
from backend.services.sorting.selection import SelectionSortProcessDataLogger


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
def selection_sort_process_data_logger(
    selection_sorter: SelectionSorter,
) -> SelectionSortProcessDataLogger:
    """Build a fresh selection-sort process logger for one test.

    Args:
        selection_sorter: Shared selection sort engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return SelectionSortProcessDataLogger(selection_sorter)


@pytest.fixture(scope="function")
def quick_sort_process_data_logger(
    quick_sorter: QuickSorter,
) -> QuickSortProcessDataLogger:
    """Build a fresh quick-sort process logger for one test.

    Args:
        quick_sorter: Shared quick sort engine fixture.

    Returns:
        Logger with an empty ``algorithm_log``.
    """
    return QuickSortProcessDataLogger(quick_sorter)


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


@pytest.fixture(scope="function")
def quick_sort_test_step_data() -> QuickSortStepValueObject:
    """Provide one sample quick-sort step for logger tests.

    Returns:
        Frozen partition step with fixed depth, pivot, and ``SORTING`` status.
    """
    step_data = QuickSortStepValueObject(
        depth=1,
        side=RecursionTreeSide.ROOT,
        pivot=38,
        before=(2, 38, 3, 33, -4),
        result=([-4, 2], [3], [33, 38]),
        status=SortingStatus.SORTING,
    )

    return step_data


@pytest.fixture(scope="function")
def selection_sort_test_step_data() -> BaseSortStepValueObject:
    """Provide one sample selection-sort step for logger tests.

    Returns:
        Frozen step with fixed index, value, and ``SORTING`` status.
    """
    step_data: BaseSortStepValueObject = BaseSortStepValueObject(
        index=0,
        value=2,
        before=(2, 38, 3, 42, 1),
        result=(1, 3, 38, 42, 2),
        status=SortingStatus.SORTING,
    )

    return step_data


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
def expected_quick_sort_log_fields() -> tuple[str, ...]:
    """Field names that quick sort process log must fill.

    Returns:
        Tuple of column names on ``QuickSortAlgorithmLogDTO``.
    """
    return (
        Fields.DEPTH,
        Fields.SIDE,
        Fields.PIVOT,
        Fields.BEFORE,
        Fields.RESULT,
        Fields.SORT_STATUS,
    )
