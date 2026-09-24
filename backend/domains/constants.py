from enum import StrEnum


class SortingStatus(StrEnum):
    """Simple labels for "still sorting" vs "done".

    Attributes:
        SORTING: We are still moving numbers around.
        READY: The whole list is sorted.
    """

    SORTING = "sorting"
    READY = "ready"


class BinarySearchStatus(StrEnum):
    """How the middle number compares to the target.

    Attributes:
        EQUAL: Middle number is the target.
        GREATER: Middle number is bigger than the target.
        LESS: Middle number is smaller than the target.
    """

    EQUAL = "equal to"
    GREATER = "greater than"
    LESS = "less than"
