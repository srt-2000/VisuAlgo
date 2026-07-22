"""Domain types for sorting step visualization."""

from dataclasses import dataclass
from enum import StrEnum


class SortingStatus(StrEnum):
    """Simple labels for “still sorting” vs “done”."""

    SORTING = "sorting"
    READY = "ready"


@dataclass(frozen=True, slots=True)
class InsertionSortStepValueObject:
    """One frozen photo of an insertion-sort step.

    Attributes:
        index: Where we are looking right now.
        value: The number we are placing.
        sort_state: How the whole list looks at this moment.
        status: Whether we are still sorting or already finished.
    """

    index: int
    value: int
    sort_state: tuple[int, ...]
    status: SortingStatus
