"""Session keys and short labels for the insertion-sort page."""

from enum import StrEnum


class Fields(StrEnum):
    """Keys stored in ``st.session_state`` and process data."""

    NOT_SORTED_ARRAY = "not_sorted_array"
    SORTED_ARRAY = "sorted_array"
    PROCESS_DATA = "process_data"
    RESULT = "result"


class Messages(StrEnum):
    """Short captions above the unsorted and sorted lists."""

    NOT_SORTED_ARRAY = "NOT sorted array"
    SORTED_ARRAY = "SORTED array"
