"""Service that logs binary search steps for UI visualization."""

from collections import defaultdict

from loguru import logger

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.constants import Fields, Messages, addition_to_full_range
from services.exceptions import TargetIndexNotFoundException


class BinarySearchProcessDataLogger:
    """Runs binary search and accumulates human-readable step logs.

    Attributes:
        search_log: Mapping from log field name to per-step string values.
    """

    def __init__(self, searcher_object: BinarySearch) -> None:
        """Initialize the logger with a binary search engine.

        Args:
            searcher_object: Algorithm instance used to iterate search steps.
        """
        self._search_engine: BinarySearch = searcher_object
        self.search_log: defaultdict[str, list[str]] = defaultdict(list)

    def _record_step_data_to_search_log(
        self,
        step_data: BinarySearchStepValueObject,
        array: list[int],
    ) -> None:
        """Append one step snapshot to ``search_log``.

        Args:
            step_data: Current binary search step value object.
            array: Sorted array being searched (used for range labels).
        """
        self.search_log[Fields.STEP_RANGE].append(
            f"{array[step_data.left_index]} ... {array[step_data.right_index]}"
        )
        self.search_log[Fields.RANGE_SIZE].append(
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} "
            f"{Fields.PIECES}"
        )
        self.search_log[Fields.MIDDLE_INDEX].append(str(step_data.mid_index))
        self.search_log[Fields.MIDDLE_ELEMENT].append(str(step_data.middle_value))
        self.search_log[Fields.STATUS].append(step_data.status)
        self.search_log[Fields.TARGET].append(str(step_data.target))

    def search_and_get_process_data(
        self,
        array: list[int],
        target: int,
    ) -> defaultdict[str, list[str]]:
        """Run binary search and return the accumulated process log.

        Clears any previous log, records every comparison step, and returns
        the filled ``search_log`` when ``target`` is found.

        Args:
            array: Sorted list of integers to search.
            target: Value to locate.

        Returns:
            Log mapping field names to lists of per-step string values.

        Raises:
            TargetIndexNotFoundException: If ``target`` is not present in
                ``array``.
        """
        self.search_log.clear()
        target_index: int | None = None

        for step_data in self._search_engine.iter_steps(array, target):
            self._record_step_data_to_search_log(step_data, array)

            if step_data.status == BinarySearchStatus.EQUAL:
                target_index = step_data.mid_index

        if target_index is None:
            logger.warning(Messages.INDEX_NOT_FOUND)
            raise TargetIndexNotFoundException(target)

        return self.search_log
