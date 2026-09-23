"""Shared page titles and Material icons for the UI."""

from enum import StrEnum
from typing import Literal


class PageTitle(StrEnum):
    """Browser tab titles for each app page."""

    ABOUT = "About Visualgo"
    BINARY_SEARCH_ALGORITHM = "Binary Search Algorithm"
    INSERTION_SORT_ALGORITHM = "Insertion Sort Algorithm"


class Icon(StrEnum):
    """Streamlit Material icon tokens used across pages."""

    INFO = ":material/info:"
    SEARCH_CHECK = ":material/search_check_2:"
    CHECK = ":material/check:"
    SORT = ":material/sort:"
    INPUT = ":material/input:"
    DONE_OUTLINE = ":material/done_outline:"


class SliderLiteral:
    """Literal values passed to Streamlit slider options."""

    QUERY_PARAMS: Literal["query-params"] = "query-params"


class TableBorderLiteral:
    """Border style token for ``st.table``."""

    HORIZONTAL_BORDER: Literal["horizontal"] = "horizontal"
