"""Domain types for sorting step visualization."""

from dataclasses import dataclass, field

from backend.domains.base import BaseAlgorithmLogDTO


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
    status: str


@dataclass
class InsertionSortAlgorithmLogDTO(BaseAlgorithmLogDTO):
    """Column-oriented log of one insertion-sort run.

    Each list grows by one item every time a value is inserted.

    Attributes:
        index: Cursor index at each step.
        value: Value being inserted at each step.
        before: How the list looked before this move.
        result: How the list looks after this move.
        status: ``sorting`` while work remains, ``ready`` on the last step.
    """

    index: list[int] = field(default_factory=list)
    value: list[int] = field(default_factory=list)
    before: list[tuple[int, ...]] = field(default_factory=list)
    result: list[tuple[int, ...]] = field(default_factory=list)
    status: list[str] = field(default_factory=list)
