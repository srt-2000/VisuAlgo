"""UI labels and widget defaults for the binary-search page."""

from enum import StrEnum, IntEnum
from typing import Literal



class Header(StrEnum):
    """Page header text and divider color."""

    BINARY_SEARCH = "BINARY SEARCH"
    DIVIDER = "green"


class SliderInt(IntEnum):
    """Numeric limits for the sorted-list range slider."""

    MIN = 1
    MAX = 1000
    START_RENDER_MIN = 300
    START_RENDER_MAX = 800


class SliderStr(StrEnum):
    """Text keys and label for the range slider."""

    LIST_RANGE_LENGTH = "list_range_length"
    LABEL = "Define your sorted list range on the slider scale"


class Badge(StrEnum):
    """Badge text shown above the target input."""

    SORTED_LIST_LABEL = (
        "You defined **0-indexed** and sorted list with elements numbers range "
    )


class BadgeColor:
    """Allowed badge color token."""

    GREEN: Literal["green"] = "green"


class NumberInputStr(StrEnum):
    """Text label and session key for the target number input."""

    LABEL = "Input a TARGET number value"
    KEY_INPUTTED_TARGET = "inputted_target"


class NumberInputInt(IntEnum):
    """Step size for the target number input."""

    STEP = 1


class Button(StrEnum):
    """Label for the search action button."""

    LABEL = "Find the target number index"


class Error(StrEnum):
    """Error text when the target is missing."""

    NOT_FOUND_MESSAGE = "element not found after algorithm's work"


class Success(StrEnum):
    """Success text prefix before the found index."""

    SUCCESS_MESSAGE = "element has index"
