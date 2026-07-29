"""Shared labels and messages for algorithm process logs."""

from enum import StrEnum

addition_to_full_range: int = 1
"""Add this so inclusive left..right indices count as a full length."""


class Fields(StrEnum):
    """Column names written into algorithm process logs."""

    STEP_RANGE = "step range"
    RANGE_SIZE = "range size"
    PIECES = "psc"
    MIDDLE_INDEX = "middle index"
    MIDDLE_ELEMENT = "middle number"
    STATUS = "check status to"
    TARGET = "target"
    INDEX = "index"
    VALUE = "value"
    SORT_STATUS = "status"
    RESULT = "result"
    BEFORE = "before"


class Messages(StrEnum):
    """Short text pieces used in logs and error messages."""

    INDEX_NOT_FOUND = "index not found"
    TARGET_NUMBER = "target number"
