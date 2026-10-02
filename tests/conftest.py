"""Shared pytest fixtures for VisuAlgo tests."""

from dataclasses import dataclass

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.base import BaseAlgorithmLogDTO


@pytest.fixture(scope="function")
def empty_list() -> list[int]:
    """Provide an empty list for edge-case tests.

    Returns:
        Empty list.
    """
    return []


@pytest.fixture(scope="class")
def binary_searcher() -> BinarySearch:
    """Give tests one shared ``BinarySearch`` instance.

    Returns:
        A binary search algorithm object.
    """
    return BinarySearch()


@pytest.fixture(scope="class")
def insertion_sorter() -> InsertionSorter:
    """Give tests one shared ``InsertionSorter`` instance.

    Returns:
        An insertion sort algorithm object.
    """
    return InsertionSorter()


@dataclass
class AlgorithmLogDTO(BaseAlgorithmLogDTO):
    """Test log with four text columns and no field defaults.

    ``clear()`` turns each column into ``None`` because nothing here
    was declared with a default value.

    Attributes:
        column1: First text column.
        middle_index: Middle indexes stored as text.
        check_status: Comparison labels such as ``>``, ``<``, ``=``.
        target: Target values stored as text.
    """

    column1: list[str]
    middle_index: list[str]
    check_status: list[str]
    target: list[str]


@pytest.fixture(scope="function")
def algorithm_log_dto() -> AlgorithmLogDTO:
    """Build a filled log for dataframe and ``clear()`` tests.

    Returns:
        Log whose four columns each hold three values.
    """
    log_dto = AlgorithmLogDTO(
        column1=["par1_1", "par1_2", "par1_3"],
        middle_index=["0", "2", "3"],
        check_status=[">", "<", "="],
        target=["7", "7", "7"],
    )

    return log_dto
