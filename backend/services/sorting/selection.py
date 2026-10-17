"""Turn selection-sort steps into readable logs for the UI."""

from loguru import logger

from backend.algorithms.sorting.selection import SelectionSorter
from backend.domains.sorting import BaseSortAlgorithmLogDTO, BaseSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError


class SelectionSortProcessDataLogger:
    """Run selection sort and keep a readable log of each step.

    Attributes:
        algorithm_log: One list per column. Each outer pass appends one item.
    """

    def __init__(self, algorithm: SelectionSorter) -> None:
        """Store the algorithm engine and start with an empty log.

        Args:
            algorithm: Engine that yields step snapshots via ``iter_steps``.
        """
        self._algorithm_engine = algorithm
        self.algorithm_log = BaseSortAlgorithmLogDTO()

    def _record_step_data_to_algorithm_log(
        self,
        step_data: BaseSortStepValueObject,
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
    ) -> BaseSortAlgorithmLogDTO:
        """Sort a copy of ``array`` and return the filled step log.

        Clears any old log first.

        Args:
            array: List of ints to sort.

        Returns:
            The same log object, now filled with one entry per outer pass.
        """
        self.algorithm_log.clear()

        for step_data in self._algorithm_engine.iter_steps(array):
            self._record_step_data_to_algorithm_log(step_data)

        return self.algorithm_log

    def get_result_array_from_process_log(self) -> tuple[int, ...]:
        """Return the array snapshot from the last step in the log.

        After a finished sort that snapshot is the sorted list.

        Returns:
            How the list looked after the final pass.

        Raises:
            EmptyResultInProcessLogError: If the log has no steps yet.
        """
        try:
            result_array: tuple[int, ...] = self.algorithm_log.result[-1]
        except IndexError:
            logger.warning(Messages.EMPTY_RESULT_IN_LOG)
            raise EmptyResultInProcessLogError() from None

        return result_array
