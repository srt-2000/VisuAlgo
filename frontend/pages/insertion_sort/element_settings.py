"""UI labels and widget defaults for the insertion-sort page."""

from enum import StrEnum, IntEnum
from typing import Literal


class Header(StrEnum):
    """Page header text and divider color."""

    INSERTION_SORT = "INSERTION SORT"
    DIVIDER = "yellow"


class Columns(IntEnum):
    """How many Streamlit columns each layout row uses."""

    RANDOM_LIST_DATA_COLUMNS_QUANTITY = 3
    LIST_RENDER_COLUMNS_QUANTITY = 2


class NumberInputStr(StrEnum):
    """Labels and placeholder for random-list number inputs."""

    LABEL_LENGTH = "length"
    LABEL_MIN_VALUE = "minimum value"
    LABEL_MAX_VALUE = "maximum value"
    PLACEHOLDER_ENTER_NUMBER = "Enter a number"


class LeftColumnNumberInputInt(IntEnum):
    """Limits for the list-length input (left column)."""

    MIN = 0
    MAX = 50
    RENDER = 3
    STEP = 1


class MidColumnNumberInputInt(IntEnum):
    """Limits for the minimum-value input (middle column)."""

    MIN = -100
    MAX = 100
    RENDER = -90
    STEP = 1


class RightColumnNumberInputInt(IntEnum):
    """Limits for the maximum-value input (right column)."""

    MAX = 100
    RENDER = 90
    STEP = 1


class Button(StrEnum):
    """Label for the sort action button."""

    LABEL_SORT_IT = "SORT IT"


class TableBorder:
    """Border style token for ``st.table``."""

    HORIZONTAL_BORDER: Literal["horizontal"] = "horizontal"


class DataFrameStr(StrEnum):
    """Row-label prefix for the steps table."""

    AXIS_NAME = "step"


class DataFrameInt(IntEnum):
    """Axis index used when renaming DataFrame rows."""

    AXIS_LINES_CHANGES_PARAMETER = 0
