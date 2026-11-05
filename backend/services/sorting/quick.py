"""Turn quick-sort steps into readable logs for the UI."""

from loguru import logger

from backend.algorithms.sorting.quick import QuickSorter
from backend.domains.sorting import QuickSortAlgorithmLogDTO, QuickSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError


class QuickSortProcessDataLogger:
    """Run quick sort and keep a readable log of each step.

    Attributes:
        algorithm_log: One list per column. Each partition appends one item.
    """

    def __init__(self, algorithm: QuickSorter) -> None:
        """Store the algorithm engine and start with an empty log.

        Args:
            algorithm: Engine that yields step snapshots via ``iter_steps``.
        """
        self._algorithm_engine = algorithm
        self.algorithm_log = QuickSortAlgorithmLogDTO()

    def _record_step_data_to_algorithm_log(
        self,
        step_data: QuickSortStepValueObject,
    ) -> None:
        """Append one step's fields into ``algorithm_log``.

        Args:
            step_data: Current sort step.
        """
        self.algorithm_log.depth.append(step_data.depth)
        self.algorithm_log.side.append(step_data.side)
        self.algorithm_log.pivot.append(step_data.pivot)
        self.algorithm_log.before.append(step_data.before)
        self.algorithm_log.result.append(step_data.result)
        self.algorithm_log.status.append(step_data.status)

    def get_result_and_process_data(
        self,
        array: list[int],
    ) -> QuickSortAlgorithmLogDTO:
        """Sort a copy of ``array`` and return the filled step log.

        Clears any old log first.

        Args:
            array: List of ints to sort.

        Returns:
            The same log object, now filled with one entry per partition step.
        """
        self.algorithm_log.clear()

        for step_data in self._algorithm_engine.iter_steps(array):
            self._record_step_data_to_algorithm_log(step_data)

        return self.algorithm_log

    def get_result_array_from_process_log(self) -> tuple[list[int], ...]:
        """Return the partition snapshot from the last step in the log.

        After a finished root run that snapshot is the final
        ``(left, middle, right)`` buckets that form the sorted list.

        Returns:
            Last ``result`` triple written into the log.

        Raises:
            EmptyResultInProcessLogError: If the log has no steps yet.
        """
        try:
            result_array: tuple[list[int], ...] = self.algorithm_log.result[-1]
        except IndexError:
            logger.warning(Messages.EMPTY_RESULT_IN_LOG)
            raise EmptyResultInProcessLogError() from None

        return result_array
