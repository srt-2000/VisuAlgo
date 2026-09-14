"""Abstract base for services that log algorithm steps for the UI."""

from abc import ABC, abstractmethod
from collections import defaultdict

from backend.algorithms.interfaces import AlgorithmBase


class ServiceBase(ABC):
    """Wrap an algorithm engine and accumulate a human-readable step log.

    Attributes:
        algorithm_log: Field name → list of per-step values.
    """

    def __init__(self, algorithm: AlgorithmBase) -> None:
        """Store the algorithm engine and start with an empty log.

        Args:
            algorithm: Engine that yields step snapshots via ``iter_steps``.
        """
        self._algorithm_engine = algorithm
        self.algorithm_log: defaultdict[str, list[int | str | tuple]] = defaultdict(
            list
        )

    @abstractmethod
    def _record_step_data_to_algorithm_log(self, *args, **kwargs) -> None:
        """Append one step's fields into ``algorithm_log``.

        Args:
            *args: Step payload and any context the subclass needs.
            **kwargs: Optional recording options.
        """
        pass

    @abstractmethod
    def get_result_and_process_data(
        self, *args, **kwargs
    ) -> defaultdict[str, list[str]]:
        """Run the algorithm, fill ``algorithm_log``, and return it.

        Args:
            *args: Algorithm inputs (array, target, ...).
            **kwargs: Optional run options.

        Returns:
            Log map: field name → list of per-step values.
        """
        pass
