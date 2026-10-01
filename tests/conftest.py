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
    """Give tests one shared ``BaseAlgorithmLogDTO`` instance."""
    column1: list[str]
    middle_index: list[str]
    check_status: list[str]
    target: list[str]


@pytest.fixture(scope="function")
def log_dto() -> AlgorithmLogDTO:
    """Give tests ``AlgorithmLogDTO`` instance.

    Returns:
        An algorithm LOG object.
    """
    log_dto = AlgorithmLogDTO(
        column1=["par1_1", "par1_2", "par1_3"],
        middle_index=["0", "2", "3"],
        check_status=[">", "<", "="],
        target=["7", "7", "7"],
    )

    return log_dto
