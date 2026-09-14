"""Fixed inputs for ``InsertionSortProcessDataLogger`` tests."""

from backend.services.constants import Fields

INSERTION_SORT_RECORD_TEST_ARRAY: list[int] = [2, 38, 3]
"""Unsorted sample list used when recording sort steps in logger tests."""

INSERTION_SORT_EXPECTED_LOG_FIELDS = (
    Fields.INDEX,
    Fields.VALUE,
    Fields.BEFORE,
    Fields.RESULT,
    Fields.SORT_STATUS,
)
"""Every field the logger must fill on each recorded step."""
