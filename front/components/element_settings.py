"""Sidebar labels and file paths for Streamlit pages."""

from enum import StrEnum
import streamlit as st


class LeftNavigationTitle(StrEnum):
    """Short titles shown in the left navigation menu."""

    ABOUT = "About"
    BINARY_SEARCH = "Binary Search"
    INSERTION_SORT = "Insertion Sort"


pages_paths = st.secrets.project_pages_paths
