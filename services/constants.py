"""Shared string constants for binary search logging and messages."""

from enum import StrEnum

addition_to_full_range: int = 1
"""Offset that converts inclusive index bounds into an element count."""


class Fields(StrEnum):
    """Column / field names used in the binary search process log."""

    STEP_RANGE = "step range"
    RANGE_SIZE = "range size"
    PIECES = "psc"
    MIDDLE_INDEX = "middle index"
    MIDDLE_ELEMENT = "middle number"
    STATUS = "check status to"
    TARGET = "target"


class Messages(StrEnum):
    """User-facing and log message fragments."""

    INDEX_NOT_FOUND = "index not found"
    TARGET_NUMBER = "target number"
