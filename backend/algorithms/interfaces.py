"""Abstract base for step-yielding algorithm engines."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, TypeVar, Generic, Optional

T = TypeVar("T", bound=dataclass)


class AlgorithmBase(ABC, Generic[T]):
    """Base for algorithms that expose step-by-step iteration.

    Subclasses implement ``iter_steps`` and may add a thin entry point
    such as ``search`` or ``sort``.
    """

    @staticmethod
    @abstractmethod
    def iter_steps(*args, **kwargs) -> Iterator[Optional[T]]:
        """Yield frozen step snapshots while the algorithm runs.

        Args:
            *args: Algorithm-specific inputs (array, target, ...).
            **kwargs: Optional algorithm-specific options.

        Yields:
            One step value object per meaningful step, or ``None`` when
            a subclass uses an empty/optional step.
        """
        pass
