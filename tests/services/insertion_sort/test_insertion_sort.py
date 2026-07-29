"""Unit tests for ``InsertionSortProcessDataLogger``."""

from collections import defaultdict

import pytest

from algorithms.insertion_sort import InsertionSorter
from domains.sorting import InsertionSortStepValueObject, SortingStatus
from services.constants import Fields
from services.insertion_sort import InsertionSortProcessDataLogger
from tests.services.insertion_sort.cases import RECORD_TEST_ARRAY


class TestInsertionSortProcessDataLogger:
    """Check that the logger writes, appends, clears, and raises correctly."""

    def test_record_step_data(
        self,
        get_insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sort_test_step_data: InsertionSortStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right value."""
        logger = get_insertion_sort_process_data_logger
        step_data = insertion_sort_test_step_data

        logger._record_step_data_to_sort_log(step_data)
        step_records: defaultdict[str, list[str]] = logger.sort_log

        assert step_records[Fields.INDEX] == [int(step_data.index)]
        assert step_records[Fields.VALUE] == [int(step_data.value)]
        assert step_records[Fields.BEFORE] == [step_data.before]
        assert step_records[Fields.RESULT] == [step_data.result]
        assert step_records[Fields.SORT_STATUS] == [str(step_data.status)]

    def test_record_step_data_appends(
        self,
        get_insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sort_test_step_data: InsertionSortStepValueObject,
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = get_insertion_sort_process_data_logger
        step_data = insertion_sort_test_step_data
        expected_log_fields = (
            Fields.INDEX,
            Fields.VALUE,
            Fields.BEFORE,
            Fields.RESULT,
            Fields.SORT_STATUS,
        )
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_sort_log(step_data)

        for field in expected_log_fields:
            field_len: int = len(logger.sort_log[field])
            assert field_len == test_range

    def test_sort_and_get_process_data(
        self,
        get_insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        get_insert_sorter: InsertionSorter,
    ) -> None:
        """Finished sort ends with READY; log length matches ``iter_steps``."""
        logger = get_insertion_sort_process_data_logger
        sorter = get_insert_sorter
        process_data: defaultdict[str, list[str]] = logger.sort_and_get_process_data(
            RECORD_TEST_ARRAY,
        )
        end_status: str = process_data[Fields.SORT_STATUS][-1]
        index_field_len = len(process_data[Fields.INDEX])
        steps_quantity = len(list(sorter.iter_steps(RECORD_TEST_ARRAY)))

        assert end_status == SortingStatus.READY
        assert index_field_len == steps_quantity

    def test_sort_and_log_process_data_with_none(
        self,
        get_insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
    ) -> None:
        """Passing ``None`` instead of a list must raise ``TypeError``."""
        with pytest.raises(TypeError):
            logger = get_insertion_sort_process_data_logger
            logger.sort_and_get_process_data(None)

    def test_sort_to_clean_previous_log(
        self,
        get_insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
    ) -> None:
        """A second sort must replace the old log, not grow it."""
        logger = get_insertion_sort_process_data_logger
        first_log = logger.sort_and_get_process_data(RECORD_TEST_ARRAY)
        first_log_len = len(first_log[Fields.VALUE])
        second_log = logger.sort_and_get_process_data(RECORD_TEST_ARRAY)
        second_log_len = len(second_log[Fields.VALUE])
        assert second_log_len == first_log_len
