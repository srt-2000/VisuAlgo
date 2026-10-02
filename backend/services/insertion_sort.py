"""Turn insertion-sort steps into readable logs for the UI."""

from loguru import logger

from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.insertion_sort import InsertionSortAlgorithmLogDTO, InsertionSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError


class InsertionSortProcessDataLogger:
    """Run insertion sort and keep a readable log of each step.

    Attributes:
        algorithm_log: One list per column. Each insertion appends one item.
    """

    def __init__(self, algorithm: InsertionSorter) -> None:
        """Store the algorithm engine and start with an empty log.

        Args:
            algorithm: Engine that yields step snapshots via ``iter_steps``.
        """
        self._algorithm_engine = algorithm
        self.algorithm_log = InsertionSortAlgorithmLogDTO()

    def _record_step_data_to_algorithm_log(
        self,
        step_data: InsertionSortStepValueObject,
    ) -> None:
        """Append one step's fields into ``algorithm_log``.

        Args:
            step_data: Current sort step.
        """
        self.algorithm_log.index.append(step_data.index)
        self.algorithm_log.value.append(step_data.value)
        self.algorithm_log.before.append(step_data.before)
        self.algorithm_log.result.append(step_data.result)
        self.algorithm_log.status.append(step_data.status)

    def get_result_and_process_data(
        self,
        array: list[int],
    ) -> InsertionSortAlgorithmLogDTO:
        """Sort a copy of ``array`` and return the filled step log.

        Clears any old log first.

        Args:
            array: List of ints to sort.

        Returns:
            The same log object, now filled with one entry per insertion.
        """
        self.algorithm_log.clear()

        for step_data in self._algorithm_engine.iter_steps(array):
            self._record_step_data_to_algorithm_log(step_data)

        return self.algorithm_log

    def get_result_array_from_process_log(self) -> tuple[int, ...]:
        """Return the array snapshot from the last step in the log.

        After a finished sort that snapshot is the sorted list.

        Returns:
            How the list looked after the final insertion.

        Raises:
            EmptyResultInProcessLogError: If the log has no steps yet.
        """
        try:
            result_array: tuple[int, ...] = self.algorithm_log.result[-1]
        except IndexError:
            logger.warning(Messages.EMPTY_RESULT_IN_LOG)
            raise EmptyResultInProcessLogError() from None

        return result_array
