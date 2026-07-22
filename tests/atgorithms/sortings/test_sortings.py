"""Unit tests for sorting algorithms."""

import pytest

from algorithms.insertion_sort import InsertionSorter
from tests.atgorithms.sortings.cases import NOT_SORTED_ARRAYS


class TestSorters:
    """Check that sorters match Python’s built-in ``sorted``."""

    @pytest.mark.parametrize("array", NOT_SORTED_ARRAYS)
    def test_insert_sort(
        self,
        get_insert_sorter: InsertionSorter,
        array: tuple[int, ...],
    ) -> None:
        """Sorted copy of ``array`` must equal ``sorted(array)``."""
        assert get_insert_sorter.sort(list(array)) == sorted(array)
