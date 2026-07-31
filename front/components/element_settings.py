"""Sidebar labels and file paths for Streamlit pages."""

from enum import StrEnum


class LeftNavigationTitle(StrEnum):
    """Short titles shown in the left navigation menu."""

    ABOUT = "About"
    BINARY_SEARCH = "Binary Search"
    INSERTION_SORT = "Insertion Sort"


class PagePath(StrEnum):
    """Relative paths to Streamlit page scripts."""

    ABOUT = "front/pages/about/page_about.py"
    BINARY_SEARCH = "front/pages/binary_search/page_binary_search.py"
    INSERTION_SORT = "front/pages/insertion_sort/page_insertion_sort.py"
