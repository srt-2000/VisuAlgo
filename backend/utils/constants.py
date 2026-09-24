from enum import StrEnum, IntEnum


class DataFrameStr(StrEnum):
    """Row-label prefix for the steps table."""

    AXIS_NAME = "step"


class DataFrameInt(IntEnum):
    """Axis index used when renaming DataFrame rows."""

    AXIS_LINES_CHANGES_PARAMETER = 0