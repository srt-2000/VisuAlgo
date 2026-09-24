"""Abstract base for step-yielding algorithm engines."""

from abc import ABC, abstractmethod
from typing import Iterator

from backend.domains.base import BaseStepValueObject


class AlgorithmBase(ABC):
    """Base for algorithms that expose step-by-step iteration.

    Subclasses implement ``iter_steps`` and may add a thin entry point
    such as ``search`` or ``sort``.
    """

    @staticmethod
    @abstractmethod
    def iter_steps(*args, **kwargs) -> Iterator[BaseStepValueObject]:
        """Yield frozen step snapshots while the algorithm runs.

        Args:
            *args: Algorithm-specific inputs (array, target, ...).
            **kwargs: Optional algorithm-specific options.

        Yields:
            One step value object per meaningful step.
        """
        pass
