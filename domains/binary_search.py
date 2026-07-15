"""Domain types for binary search step visualization."""

from dataclasses import dataclass
from enum import StrEnum


class BinarySearchStatus(StrEnum):
    """Outcome of comparing the middle element with the target."""

    EQUAL = "equal to"
    GREATER = "greater than"
    LESS = "less than"


@dataclass(frozen=True, slots=True)
class BinarySearchStepValueObject:
    """Immutable snapshot of a single binary search comparison step.

    Attributes:
        left_index: Inclusive left bound of the current search window.
        right_index: Inclusive right bound of the current search window.
        mid_index: Index of the middle element inspected in this step.
        middle_value: Value at ``mid_index``.
        status: Result of comparing ``middle_value`` with ``target``.
        target: Value being searched for.
    """

    left_index: int
    right_index: int
    mid_index: int
    middle_value: int
    status: BinarySearchStatus
    target: int
