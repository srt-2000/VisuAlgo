from enum import StrEnum


class SortingStatus(StrEnum):
    """Simple labels for "still sorting" vs "done".

    Attributes:
        SORTING: We are still moving numbers around.
        READY: The whole list is sorted.
    """

    SORTING = "sorting"
    READY = "ready"
