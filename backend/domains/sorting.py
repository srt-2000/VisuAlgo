"""Domain types for sorting step visualization."""

from dataclasses import dataclass

from backend.utils.constants import SortingStatus


@dataclass(frozen=True, slots=True)
class InsertionSortStepValueObject:
    """One frozen photo of an insertion-sort step.

    Attributes:
        index: Where we are looking right now.
        value: The number we are placing.
        before: How the list looked right before this move.
        result: How the whole list looks at this moment.
        status: Whether we are still sorting or already finished.
    """

    index: int
    value: int
    before: tuple[int, ...]
    result: tuple[int, ...]
    status: SortingStatus
