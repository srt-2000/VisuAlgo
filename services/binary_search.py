"""Turn binary-search steps into readable logs for the UI."""

from collections import defaultdict

from loguru import logger

from algorithms.interfaces import AlgorithmBase
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.constants import Fields, Messages, addition_to_full_range
from services.exceptions import TargetIndexNotFoundException
from services.interfaces import ServiceBase


class BinarySearchProcessDataLogger(ServiceBase):
    """Run binary search and keep a human-readable log of each step.

    Attributes:
        algorithm_log: Field name → list of string values, one per step.
    """

    def __init__(self, algorithm: AlgorithmBase) -> None:
        """Store the search engine used to walk through steps.

        Args:
            algorithm: Binary search algorithm instance.
        """
        super().__init__(algorithm)
        self._algorithm_engine: AlgorithmBase = algorithm
        self.algorithm_log: defaultdict[str, list[str]] = defaultdict(list)

    def _record_step_data_to_algorithm_log(
        self,
        step_data: BinarySearchStepValueObject,
        array: list[int],
    ) -> None:
        """Append one step's text fields into ``algorithm_log``.

        Args:
            step_data: Current search step.
            array: Sorted list being searched (used for range labels).
        """
        self.algorithm_log[Fields.STEP_RANGE].append(
            f"{array[step_data.left_index]} ... {array[step_data.right_index]}"
        )
        self.algorithm_log[Fields.RANGE_SIZE].append(
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} "
            f"{Fields.PIECES}"
        )
        self.algorithm_log[Fields.MIDDLE_INDEX].append(str(step_data.mid_index))
        self.algorithm_log[Fields.MIDDLE_ELEMENT].append(str(step_data.middle_value))
        self.algorithm_log[Fields.STATUS].append(step_data.status)
        self.algorithm_log[Fields.TARGET].append(str(step_data.target))

    def get_result_and_process_data(
        self,
        array: list[int],
        target: int,
    ) -> defaultdict[str, list[str]]:
        """Search for ``target`` and return the filled step log.

        Clears any old log first. Raises if ``target`` is not found.

        Args:
            array: Sorted list of ints.
            target: Number to find.

        Returns:
            Log map: field name → list of per-step strings.

        Raises:
            TargetIndexNotFoundException: If ``target`` is missing from
                ``array``.
        """
        self.algorithm_log.clear()
        target_index: int | None = None

        for step_data in self._algorithm_engine.iter_steps(array, target):
            self._record_step_data_to_algorithm_log(step_data, array)

            if step_data.status == BinarySearchStatus.EQUAL:
                target_index = step_data.mid_index

        if target_index is None:
            logger.warning(Messages.INDEX_NOT_FOUND)
            raise TargetIndexNotFoundException(target)

        return self.algorithm_log
