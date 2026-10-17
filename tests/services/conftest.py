"""Pytest fixtures shared by service-layer unit tests."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.domains.binary_search import BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus
from backend.services.binary_search import BinarySearchProcessDataLogger


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
