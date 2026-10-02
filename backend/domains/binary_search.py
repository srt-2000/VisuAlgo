"""Domain types for binary search step visualization."""

from dataclasses import dataclass, field

from backend.domains.base import BaseAlgorithmLogDTO


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
    left_value: int
    right_index: int
    right_value: int
    mid_index: int
    middle_value: int
    status: str
    target: int


@dataclass
class BinarySearchAlgorithmLogDTO(BaseAlgorithmLogDTO):
    """Column-oriented log of one binary-search run.
    Attributes:

    """

    step_range: list[str] = field(default_factory=list)
    range_size: list[str] = field(default_factory=list)
    mid_index: list[int] = field(default_factory=list)
    middle_value: list[int] = field(default_factory=list)
    status: list[str] = field(default_factory=list)
    target: list[int] = field(default_factory=list)
