"""Turn insertion-sort steps into readable logs for the UI."""

from collections import defaultdict

from loguru import logger

from backend.algorithms.interfaces import AlgorithmBase
from backend.domains.sorting import InsertionSortStepValueObject
from backend.services.constants import Fields, Messages
from backend.services.exceptions import EmptyResultInProcessLog
from backend.services.interfaces import ServiceBase


class InsertionSortProcessDataLogger(ServiceBase):
    """Run insertion sort and keep a human-readable log of each step.

    Attributes:
        algorithm_log: Field name → list of values, one per step.
    """

    def __init__(self, algorithm: AlgorithmBase) -> None:
        """Store the sorter used to walk through steps.

        Args:
            algorithm: Insertion sort algorithm instance.
        """
        super().__init__(algorithm)
        self._algorithm_engine: AlgorithmBase = algorithm
        self.algorithm_log: defaultdict[str, list[int | str | tuple]] = defaultdict(
            list
        )

    def _record_step_data_to_algorithm_log(
        self,
        step_data: InsertionSortStepValueObject,
    ) -> None:
        """Append one step's fields into ``algorithm_log``.

        Args:
            step_data: Current sort step.
        """
        self.algorithm_log[Fields.INDEX].append(int(step_data.index))
        self.algorithm_log[Fields.VALUE].append(int(step_data.value))
        self.algorithm_log[Fields.BEFORE].append(step_data.before)
        self.algorithm_log[Fields.RESULT].append(step_data.result)
        self.algorithm_log[Fields.SORT_STATUS].append(str(step_data.status))

    def get_result_and_process_data(
        self,
        array: list[int],
    ) -> defaultdict[str, list[int | str | tuple]]:
        """Sort ``array`` in place and return the filled step log.

        Clears any old log first.

        Args:
            array: List of ints to sort.

        Returns:
            Log map: field name → list of per-step values.
        """
        self.algorithm_log.clear()

        for step_data in self._algorithm_engine.iter_steps(array):
            self._record_step_data_to_algorithm_log(step_data)

        return self.algorithm_log

    def get_result_array_from_process_log(self)-> tuple[int,...]:
        """Get result sorted array from algorithm log."""
        try:
            result_array: tuple[int,...] = self.algorithm_log[Fields.RESULT][-1]
        except IndexError:
            logger.warning(Messages.EMPTY_RESULT_IN_LOG)
            raise EmptyResultInProcessLog()

        return result_array
