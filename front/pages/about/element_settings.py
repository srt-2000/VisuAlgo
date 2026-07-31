"""UI labels for the About page header."""

from enum import StrEnum


class Header(StrEnum):
    """Welcome header text and divider style."""

    WELCOME_MESSAGE = "WELCOME to Visualgo!"
    DIVIDER = "rainbow"
    HELP_INFO = "To use Visualgo select an algorithm from the sidebar and try it"
