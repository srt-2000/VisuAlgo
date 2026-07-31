"""Unit tests for ``BinarySearchProcessDataLogger``."""

from collections import defaultdict

import pytest

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.binary_search import BinarySearchProcessDataLogger
from services.constants import Fields, addition_to_full_range
from services.exceptions import TargetIndexNotFoundException
from tests.services.binary_search.cases import (
    BINARY_SEARCH_RECORD_TEST_ARRAY,
    TEST_TARGET,
    BINARY_SEARCH_EXPECTED_LOG_FIELDS,
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
        logger._record_step_data_to_search_log(
            step_data, BINARY_SEARCH_RECORD_TEST_ARRAY
        )
        step_records = logger.search_log

        expected_step_range: list[str] = [
            f"{BINARY_SEARCH_RECORD_TEST_ARRAY[step_data.left_index]} ... "
            f"{BINARY_SEARCH_RECORD_TEST_ARRAY[step_data.right_index]}"
        ]
        expected_range_size: list[str] = [
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} "
            f"{Fields.PIECES}"
        ]
        expected_middle_index: list[str] = [str(step_data.mid_index)]
        expected_middle_element: list[str] = [str(step_data.middle_value)]
        expected_status: list[str] = [step_data.status]
        expected_target: list[str] = [str(step_data.target)]

        assert step_records[Fields.STEP_RANGE] == expected_step_range
        assert step_records[Fields.RANGE_SIZE] == expected_range_size
        assert step_records[Fields.MIDDLE_INDEX] == expected_middle_index
        assert step_records[Fields.MIDDLE_ELEMENT] == expected_middle_element
        assert step_records[Fields.STATUS] == expected_status
        assert step_records[Fields.TARGET] == expected_target

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
            logger._record_step_data_to_search_log(
                step_data, BINARY_SEARCH_RECORD_TEST_ARRAY
            )

        for field in BINARY_SEARCH_EXPECTED_LOG_FIELDS:
            field_len: int = len(logger.search_log[field])
            assert field_len == test_range

    def test_search_and_get_process_data(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_searcher: BinarySearch,
    ) -> None:
        """Found target ends with EQUAL; log length matches ``iter_steps``."""
        logger = binary_search_process_data_logger
        searcher = binary_searcher
        process_data: defaultdict[str, list[str]] = logger.search_and_get_process_data(
            BINARY_SEARCH_RECORD_TEST_ARRAY,
            TEST_TARGET,
        )
        end_status: str = process_data[Fields.STATUS][-1]
        middle_index_field_len = len(process_data[Fields.MIDDLE_INDEX])
        steps_quantity = len(
            list(searcher.iter_steps(BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET))
        )

        assert end_status == BinarySearchStatus.EQUAL
        assert middle_index_field_len == steps_quantity

    def test_search_and_get_process_data_not_found(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """Missing target must raise ``TargetIndexNotFoundException``."""
        with pytest.raises(TargetIndexNotFoundException):
            logger = binary_search_process_data_logger
            array: list[int] = [1, 2, 3]
            target_not_in_array: int = 99
            logger.search_and_get_process_data(array, target_not_in_array)

    def test_search_to_clean_previous_log(
        self,
        binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """A second successful search must replace the old log, not grow it."""
        logger = binary_search_process_data_logger
        first_log = logger.search_and_get_process_data(
            BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET
        )
        first_log_len = len(first_log[Fields.MIDDLE_INDEX])
        second_log = logger.search_and_get_process_data(
            BINARY_SEARCH_RECORD_TEST_ARRAY, TEST_TARGET
        )
        second_log_len = len(second_log[Fields.MIDDLE_INDEX])
        assert second_log_len == first_log_len
