"""Domain types for binary search step visualization."""

from dataclasses import dataclass
from enum import StrEnum


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


@dataclass(frozen=True, slots=True)
class BinarySearchStepValueObject:
    """One frozen photo of a binary-search guess.

    Attributes:
        left_index: Left edge of the current search window.
        right_index: Right edge of the current search window.
        mid_index: Index of the number we just checked.
        middle_value: Value at ``mid_index``.
        status: Whether mid is equal, greater, or less than ``target``.
        target: The number we are looking for.
    """

    left_index: int
    right_index: int
    mid_index: int
    middle_value: int
    status: BinarySearchStatus
    target: int
