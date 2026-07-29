"""Turn insertion-sort steps into readable logs for the UI."""

from collections import defaultdict

from algorithms.insertion_sort import InsertionSorter
from domains.sorting import InsertionSortStepValueObject
from services.constants import Fields


class InsertionSortProcessDataLogger:
    """Run insertion sort and keep a human-readable log of each step.

    Attributes:
        sort_log: Field name → list of values, one per step.
    """

    def __init__(self, sorter: InsertionSorter) -> None:
        """Store the sorter used to walk through steps.

        Args:
            sorter: Insertion sort algorithm instance.
        """
        self._sort_engine: InsertionSorter = sorter
        self.sort_log: defaultdict[str, list[int | str | tuple]] = defaultdict(list)

    def _record_step_data_to_sort_log(
        self,
        step_data: InsertionSortStepValueObject,
    ) -> None:
        """Append one step's fields into ``sort_log``.

        Args:
            step_data: Current sort step.
        """
        self.sort_log[Fields.INDEX].append(int(step_data.index))
        self.sort_log[Fields.VALUE].append(int(step_data.value))
        self.sort_log[Fields.BEFORE].append(step_data.before)
        self.sort_log[Fields.RESULT].append(step_data.result)
        self.sort_log[Fields.SORT_STATUS].append(str(step_data.status))

    def sort_and_get_process_data(
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
        self.sort_log.clear()

        for step_data in self._sort_engine.iter_steps(array):
            self._record_step_data_to_sort_log(step_data)

        return self.sort_log
