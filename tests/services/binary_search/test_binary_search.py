"""Unit tests for ``BinarySearchProcessDataLogger``."""

import pytest

from backend.algorithms.binary_search import BinarySearch
from backend.domains.binary_search import BinarySearchAlgorithmLogDTO, BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus
from backend.services.binary_search import BinarySearchProcessDataLogger
from backend.services.constants import Fields, Messages, addition_to_full_range
from backend.services.exceptions import (
    EmptyResultInProcessLogError,
    TargetIndexNotFoundError,
)
from tests.services.binary_search.cases import (
    BINARY_SEARCH_EXPECTED_LOG_FIELDS,
    BINARY_SEARCH_RECORD_TEST_ARRAY,
    TEST_TARGET,
)


class TestBinarySearchProcessDataLogger:
    """Check that the logger writes, appends, clears, and raises correctly."""

    def test_record_step_data(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_search_test_step_data: BinarySearchStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right text."""
        logger = binary_search_process_data_logger
        step_data = binary_search_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)
        step_records = logger.algorithm_log

        expected_step_range: list[str] = [
            f"{BINARY_SEARCH_RECORD_TEST_ARRAY[step_data.left_index]} ... "
            f"{BINARY_SEARCH_RECORD_TEST_ARRAY[step_data.right_index]}"
        ]
        expected_range_size: list[str] = [
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} {Fields.PIECES}"
        ]
        expected_middle_index: list[int] = [step_data.mid_index]
        expected_middle_element: list[int] = [step_data.middle_value]
        expected_status: list[str] = [step_data.status]
        expected_target: list[int] = [step_data.target]

        assert step_records.step_range == expected_step_range
        assert step_records.range_size == expected_range_size
        assert step_records.mid_index == expected_middle_index
        assert step_records.middle_value == expected_middle_element
        assert step_records.status == expected_status
        assert step_records.target == expected_target

    def test_record_step_data_appends(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_search_test_step_data: BinarySearchStepValueObject,
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = binary_search_process_data_logger
        step_data = binary_search_test_step_data
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_algorithm_log(step_data)

        for field in BINARY_SEARCH_EXPECTED_LOG_FIELDS:
            field_len: int = len(getattr(logger.algorithm_log, field))
            assert field_len == test_range

    def test_search_and_get_process_data(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_searcher: BinarySearch,
    ) -> None:
        """Found target ends with EQUAL; log length matches ``iter_steps``."""
        logger = binary_search_process_data_logger
        searcher = binary_searcher
        process_data: BinarySearchAlgorithmLogDTO = logger.get_result_and_process_data(
            BINARY_SEARCH_RECORD_TEST_ARRAY,
            TEST_TARGET,
        )
        end_status: str = process_data.status[-1]
        middle_index_field_len = len(process_data.mid_index)
        steps_quantity = len(list(searcher.iter_steps(BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET)))

        assert end_status == BinarySearchStatus.EQUAL
        assert middle_index_field_len == steps_quantity

    def test_search_and_get_process_data_not_found(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """Missing target must raise ``TargetIndexNotFoundError``."""
        with pytest.raises(TargetIndexNotFoundError):
            logger = binary_search_process_data_logger
            array: list[int] = [1, 2, 3]
            target_not_in_array: int = 99
            logger.get_result_and_process_data(array, target_not_in_array)

    def test_search_to_clean_previous_log(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """A second successful search must replace the old log, not grow it."""
        logger = binary_search_process_data_logger
        first_log = logger.get_result_and_process_data(BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET)
        first_log_len = len(first_log.mid_index)
        second_log = logger.get_result_and_process_data(BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET)
        second_log_len = len(second_log.mid_index)
        assert second_log_len == first_log_len

    def test_get_target_index_from_result(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_search_test_step_data: BinarySearchStepValueObject,
    ) -> None:
        """The last recorded middle index is what this method returns."""
        logger = binary_search_process_data_logger
        step_data = binary_search_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)

        index_from_result: int = logger.get_target_index_from_process_log()
        expected_mid_index: int = step_data.mid_index

        assert index_from_result == expected_mid_index

    def test_get_target_index_from_empty_result(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """An empty log must raise ``EmptyResultInProcessLogError``."""
        logger = binary_search_process_data_logger

        with pytest.raises(EmptyResultInProcessLogError, match=Messages.EMPTY_RESULT_IN_LOG):
            logger.get_target_index_from_process_log()
