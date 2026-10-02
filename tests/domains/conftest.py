"""Fixtures for ``BaseAlgorithmLogDTO.clear`` tests."""

from dataclasses import dataclass

import pytest

from backend.domains.base import BaseAlgorithmLogDTO


@dataclass
class AlgorithmLogDTOWithNone(BaseAlgorithmLogDTO):
    """Test log where some columns start as ``None`` and some hold values.

    Used to check that ``clear()`` resets both kinds. These fields have
    no default, so ``clear()`` sets every one of them to ``None``.

    Attributes:
        column1: Optional first text column.
        middle_index: Optional middle-index column.
        check_status: Optional comparison labels.
        target: Optional target column.
    """

    column1: list[str] | None
    middle_index: list[str] | None
    check_status: list[str] | None
    target: list[str] | None


@pytest.fixture(scope="function")
def algorithm_log_dto_with_none() -> AlgorithmLogDTOWithNone:
    """Build a log that mixes ``None`` columns with filled ones.

    Returns:
        DTO passed into the mixed-field ``clear()`` test.
    """
    log_dto = AlgorithmLogDTOWithNone(
        column1=None,
        middle_index=["0", "2", "3"],
        check_status=None,
        target=["7", "7", "7"],
    )
    return log_dto
