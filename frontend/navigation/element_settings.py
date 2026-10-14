"""Sidebar labels and file paths for Streamlit pages."""

from enum import StrEnum

import streamlit as st


class LeftNavigationTitle(StrEnum):
    """Short titles shown in the left navigation menu."""

    ABOUT = "About"
    BINARY_SEARCH = "Binary Search"
    INSERTION_SORT = "Insertion Sort"
    BUBBLE_SORT = "Bubble Sort"


class LeftNavigationSubMenuNames(StrEnum):
    """Section titles that group pages in the left sidebar."""

    EMPTY = ""
    SEARCHING = "Searching"
    SORTING = "Sorting"


pages_paths = st.secrets.project_pages_paths
"""File paths of sidebar pages, loaded from Streamlit secrets."""
