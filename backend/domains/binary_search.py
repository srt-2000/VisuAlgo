"""Domain types for binary search step visualization."""

from dataclasses import dataclass

from backend.domains.base import BaseStepValueObject


@dataclass(frozen=True, slots=True)
class BinarySearchStepValueObject(BaseStepValueObject):
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
    status: str
    target: int
