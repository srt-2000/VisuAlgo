"""Domain types for sorting step visualization."""

from dataclasses import dataclass, field

from backend.domains.base import BaseAlgorithmLogDTO


@dataclass(frozen=True, slots=True)
class BaseSortStepValueObject:
    """One frozen photo of a sort step.

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
class BaseSortAlgorithmLogDTO(BaseAlgorithmLogDTO):
    """Column-oriented log of one sort run.

    Each list grows by one item every time the sorter yields a step.

    Attributes:
        index: Cursor index at each step.
        value: Value touched on that step.
        before: How the list looked before this move.
        result: How the list looks after this move.
        status: ``sorting`` while work remains, ``ready`` on the last step.
    """

    index: list[int] = field(default_factory=list)
    value: list[int] = field(default_factory=list)
    before: list[tuple[int, ...]] = field(default_factory=list)
    result: list[tuple[int, ...]] = field(default_factory=list)
    status: list[str] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class QuickSortStepValueObject:
    """One frozen photo of a quick-sort partition step.

    Attributes:
        depth: Current recursion depth (``0`` at the root call).
        side: Recursion-tree branch: ``root``, ``left``, or ``right``.
        pivot: Pivot value chosen for this partition.
        before: Subarray as it looked before this partition.
        result: Partition buckets as ``(left, middle, right)`` after the rearrange.
        status: ``sorting`` while work remains, ``ready`` when the root finishes.
    """

    depth: int
    side: str
    pivot: int
    before: tuple[int, ...]
    result: tuple[list[int], ...]
    status: str


@dataclass
class QuickSortAlgorithmLogDTO(BaseAlgorithmLogDTO):
    """Column-oriented log of one quick-sort run.

    Each list grows by one item every time the sorter yields a step.

    Attributes:
        depth: Recursion depth at each step.
        side: Recursion-tree branch at each step (``root``, ``left``, or ``right``).
        pivot: Pivot value used on that step.
        before: Subarray as it looked before the partition.
        result: Partition buckets ``(left, middle, right)`` after the rearrange.
        status: ``sorting`` while work remains, ``ready`` on the last root step.
    """

    depth: list[int] = field(default_factory=list)
    side: list[str] = field(default_factory=list)
    pivot: list[int] = field(default_factory=list)
    before: list[tuple[int, ...]] = field(default_factory=list)
    result: list[tuple[list[int], ...]] = field(default_factory=list)
    status: list[str] = field(default_factory=list)
