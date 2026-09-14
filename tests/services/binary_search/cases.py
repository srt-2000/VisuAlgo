"""Fixed inputs for ``BinarySearchProcessDataLogger`` tests."""

from backend.services.constants import Fields

BINARY_SEARCH_RECORD_TEST_ARRAY: list[int] = [3, 14, 26, 34, 45, 58, 59, 60, 79, 87, 92]
"""Sorted sample array used when recording and searching in logger tests."""

TEST_TARGET: int = 3
"""Target that exists in ``BINARY_SEARCH_RECORD_TEST_ARRAY``."""

BINARY_SEARCH_EXPECTED_LOG_FIELDS = (
    Fields.STEP_RANGE,
    Fields.RANGE_SIZE,
    Fields.MIDDLE_INDEX,
    Fields.MIDDLE_ELEMENT,
    Fields.STATUS,
    Fields.TARGET,
)
"""Every field the logger must fill on each recorded step."""
