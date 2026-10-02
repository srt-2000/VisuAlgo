"""Turn binary-search steps into readable logs for the UI."""

from loguru import logger

from backend.algorithms.binary_search import BinarySearch
from backend.domains.binary_search import BinarySearchAlgorithmLogDTO, BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus
from backend.services.constants import Fields, Messages, addition_to_full_range
from backend.services.exceptions import (
    EmptyResultInProcessLogError,
    TargetIndexNotFoundError,
)


class BinarySearchProcessDataLogger:
    """Run binary search and keep a readable log of each step.

    Attributes:
        algorithm_log: One list per column. Each guess appends one item.
    """

    def __init__(self, algorithm: BinarySearch) -> None:
        """Store the algorithm engine and start with an empty log.

        Args:
            algorithm: Engine that yields step snapshots via ``iter_steps``.
        """
        self._algorithm_engine = algorithm
        self.algorithm_log = BinarySearchAlgorithmLogDTO()

    def _record_step_data_to_algorithm_log(
        self,
        step_data: BinarySearchStepValueObject,
    ) -> None:
        """Append one step's fields into ``algorithm_log``.

        Args:
            step_data: Current search step.
        """
        self.algorithm_log.step_range.append(f"{step_data.left_value} ... {step_data.right_value}")
        self.algorithm_log.range_size.append(
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} {Fields.PIECES}"
        )
        self.algorithm_log.mid_index.append(step_data.mid_index)
        self.algorithm_log.middle_value.append(step_data.middle_value)
        self.algorithm_log.status.append(step_data.status)
        self.algorithm_log.target.append(step_data.target)

    def get_result_and_process_data(
        self,
        array: list[int],
        target: int,
    ) -> BinarySearchAlgorithmLogDTO:
        """Search for ``target`` and return the filled step log.

        Clears any old log first. Raises if ``target`` is not found.

        Args:
            array: Sorted list of ints.
            target: Number to find.

        Returns:
            The same log object, now filled with one entry per guess.

        Raises:
            TargetIndexNotFoundError: If ``target`` is missing from
                ``array``.
        """
        self.algorithm_log.clear()
        target_index: int | None = None

        for step_data in self._algorithm_engine.iter_steps(array, target):
            self._record_step_data_to_algorithm_log(step_data)

            if step_data.status == BinarySearchStatus.EQUAL:
                target_index = step_data.mid_index

        if target_index is None:
            logger.warning(Messages.INDEX_NOT_FOUND)
            raise TargetIndexNotFoundError(target)

        return self.algorithm_log

    def get_target_index_from_process_log(self) -> int:
        """Return the last middle index stored in the log.

        After a successful search that index is where the target sits.
        Call this only once the log has at least one step.

        Returns:
            ``mid_index`` from the last recorded step.

        Raises:
            EmptyResultInProcessLogError: If the log has no steps yet.
        """
        try:
            target_index: int = self.algorithm_log.mid_index[-1]
        except IndexError:
            logger.warning(Messages.EMPTY_RESULT_IN_LOG)
            raise EmptyResultInProcessLogError() from None

        return target_index
