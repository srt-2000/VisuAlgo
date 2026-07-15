"""Unit tests for sorting algorithms."""

import pytest

from algorithms.insertion_sort import InsertionSorter
from tests.atgorithms_tests.testcases import NOT_SORTED_ARRAYS


class TestSorters:
    """Validate sorting algorithm correctness on representative inputs."""

    @pytest.mark.parametrize("array", NOT_SORTED_ARRAYS)
    def test_insert_sort(
        self,
        insert_sorter: InsertionSorter,
        array: tuple[int, ...],
    ) -> None:
        """Sort a copy of ``array`` and match built-in ``sorted`` output."""
        assert insert_sorter.sort(list(array)) == sorted(array)
