from dataclasses import dataclass

import pytest

from backend.domains.base import BaseAlgorithmLogDTO


@dataclass
class AlgorithmLogDTOWithNone(BaseAlgorithmLogDTO):
    """Give tests one shared ``BaseAlgorithmLogDTO`` instance."""

    column1: list[str] | None
    middle_index: list[str] | None
    check_status: list[str] | None
    target: list[str] | None


@pytest.fixture(scope="function")
def algorithm_log_dto_with_none() -> AlgorithmLogDTOWithNone:
    log_dto = AlgorithmLogDTOWithNone(
        column1=None,
        middle_index=["0", "2", "3"],
        check_status=None,
        target=["7", "7", "7"],
    )
    return log_dto
