"""Turn binary-search steps into readable logs for the UI."""

from collections import defaultdict

from loguru import logger

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.constants import Fields, Messages, addition_to_full_range
from services.exceptions import TargetIndexNotFoundException


class BinarySearchProcessDataLogger:
    """Run binary search and keep a human-readable log of each step.

    Attributes:
        search_log: Field name → list of string values, one per step.
    """

    def __init__(self, searcher_object: BinarySearch) -> None:
        """Store the search engine used to walk through steps.

        Args:
            searcher_object: Binary search algorithm instance.
        """
        self._search_engine: BinarySearch = searcher_object
        self.search_log: defaultdict[str, list[str]] = defaultdict(list)

    def _record_step_data_to_search_log(
        self,
        step_data: BinarySearchStepValueObject,
        array: list[int],
    ) -> None:
        """Append one step's text fields into ``search_log``.

        Args:
            step_data: Current search step.
            array: Sorted list being searched (used for range labels).
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
