"""Column names used by the binary-search page table."""

from enum import StrEnum


class Field(StrEnum):
    """Keys that match process-log columns on this page."""

    MIDDLE_INDEX = "middle index"
