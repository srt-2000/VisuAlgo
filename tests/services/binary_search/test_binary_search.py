"""Unit tests for ``BinarySearchProcessDataLogger``."""

from collections import defaultdict

import pytest

from algorithms.binary_search import BinarySearch
from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus
from services.binary_search import BinarySearchProcessDataLogger
from services.constants import Fields, addition_to_full_range
from services.exceptions import TargetIndexNotFoundException
from tests.services.binary_search.cases import RECORD_TEST_ARRAY, TEST_TARGET


class TestBinarySearchProcessDataLogger:
    """Check that the logger writes, appends, clears, and raises correctly."""

    def test_record_step_data(
        self,
        get_binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_search_test_step_data: BinarySearchStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right text."""
        logger = get_binary_search_process_data_logger
        step_data = binary_search_test_step_data

        logger._record_step_data_to_search_log(step_data, RECORD_TEST_ARRAY)
        step_records = logger.search_log

        assert step_records[Fields.STEP_RANGE] == [
            f"{RECORD_TEST_ARRAY[step_data.left_index]} ... "
            f"{RECORD_TEST_ARRAY[step_data.right_index]}"
        ]
        assert step_records[Fields.RANGE_SIZE] == [
            f"{step_data.right_index - step_data.left_index + addition_to_full_range} "
            f"{Fields.PIECES}"
        ]
        assert step_records[Fields.MIDDLE_INDEX] == [str(step_data.mid_index)]
        assert step_records[Fields.MIDDLE_ELEMENT] == [str(step_data.middle_value)]
        assert step_records[Fields.STATUS] == [step_data.status]
        assert step_records[Fields.TARGET] == [str(step_data.target)]

    def test_record_step_data_appends(
        self,
        get_binary_search_process_data_logger: BinarySearchProcessDataLogger,
        binary_search_test_step_data: BinarySearchStepValueObject,
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = get_binary_search_process_data_logger
        step_data = binary_search_test_step_data
        expected_log_fields = (
            Fields.STEP_RANGE,
            Fields.RANGE_SIZE,
            Fields.MIDDLE_INDEX,
            Fields.MIDDLE_ELEMENT,
            Fields.STATUS,
            Fields.TARGET,
        )
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_search_log(step_data, RECORD_TEST_ARRAY)

        for field in expected_log_fields:
            field_len: int = len(logger.search_log[field])
            assert field_len == test_range

    def test_search_and_get_process_data(
        self,
        get_binary_search_process_data_logger: BinarySearchProcessDataLogger,
        get_binary_searcher: BinarySearch,
    ) -> None:
        """Found target ends with EQUAL; log length matches ``iter_steps``."""
        logger = get_binary_search_process_data_logger
        searcher = get_binary_searcher
        process_data: defaultdict[str, list[str]] = logger.search_and_get_process_data(
            RECORD_TEST_ARRAY,
            TEST_TARGET,
        )
        end_status: str = process_data[Fields.STATUS][-1]
        middle_index_field_len = len(process_data[Fields.MIDDLE_INDEX])
        steps_quantity = len(list(searcher.iter_steps(RECORD_TEST_ARRAY, TEST_TARGET)))

        assert end_status == BinarySearchStatus.EQUAL
        assert middle_index_field_len == steps_quantity

    def test_search_and_get_process_data_not_found(
        self,
        get_binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """Missing target must raise ``TargetIndexNotFoundException``."""
        with pytest.raises(TargetIndexNotFoundException):
            logger = get_binary_search_process_data_logger
            array: list[int] = [1, 2, 3]
            target_not_in_array: int = 99
            logger.search_and_get_process_data(array, target_not_in_array)

    def test_search_to_clean_previous_log(
        self,
        get_binary_search_process_data_logger: BinarySearchProcessDataLogger,
    ) -> None:
        """A second successful search must replace the old log, not grow it."""
        logger = get_binary_search_process_data_logger
        first_log = logger.search_and_get_process_data(RECORD_TEST_ARRAY, TEST_TARGET)
        first_log_len = len(first_log[Fields.MIDDLE_INDEX])
        second_log = logger.search_and_get_process_data(RECORD_TEST_ARRAY, TEST_TARGET)
        second_log_len = len(second_log[Fields.MIDDLE_INDEX])
        assert second_log_len == first_log_len
