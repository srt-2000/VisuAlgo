"""Unit tests for ``BaseAlgorithmLogDTO.clear``."""

from tests.conftest import AlgorithmLogDTO
from tests.domains.conftest import AlgorithmLogDTOWithNone


class TestBaseAlgorithmLogDTO:
    """Check that ``clear()`` resets fields that were declared without a default."""

    def test_base_algorithm_log_dto(self, algorithm_log_dto: AlgorithmLogDTO) -> None:
        """Filled lists become ``None``, because these fields have no default."""
        assert algorithm_log_dto.column1 is not None
        assert algorithm_log_dto.middle_index is not None
        assert algorithm_log_dto.check_status is not None
        assert algorithm_log_dto.target is not None

        algorithm_log_dto.clear()
        assert algorithm_log_dto.column1 is None
        assert algorithm_log_dto.middle_index is None
        assert algorithm_log_dto.check_status is None
        assert algorithm_log_dto.target is None

    def test_base_algorithm_log_dto_with_none(self, algorithm_log_dto_with_none: AlgorithmLogDTOWithNone) -> None:
        """``None`` stays ``None``, and a filled list with no default also becomes ``None``."""
        log = algorithm_log_dto_with_none
        assert log.column1 is None
        assert log.middle_index is not None
        assert log.check_status is None
        assert log.target is not None

        log.clear()
        assert log.column1 is None
        assert log.middle_index is None
        assert log.check_status is None
        assert log.target is None
