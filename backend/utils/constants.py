from enum import StrEnum, IntEnum


class SortingStatus(StrEnum):
    """Simple labels for "still sorting" vs "done".

    Attributes:
        SORTING: We are still moving numbers around.
        READY: The whole list is sorted.
    """

    SORTING = "sorting"
    READY = "ready"

class DataFrameStr(StrEnum):
    """Row-label prefix for the steps table."""

    AXIS_NAME = "step"


class DataFrameInt(IntEnum):
    """Axis index used when renaming DataFrame rows."""

    AXIS_LINES_CHANGES_PARAMETER = 0