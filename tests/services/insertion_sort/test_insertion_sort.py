"""Unit tests for ``InsertionSortProcessDataLogger``."""

import pytest

from backend.algorithms.insertion_sort import InsertionSorter
from backend.domains.constants import SortingStatus
from backend.domains.insertion_sort import InsertionSortAlgorithmLogDTO, InsertionSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError
from backend.services.insertion_sort import InsertionSortProcessDataLogger
from tests.services.insertion_sort.cases import (
    INSERTION_SORT_EXPECTED_LOG_FIELDS,
    INSERTION_SORT_RECORD_TEST_ARRAY,
)


class TestInsertionSortProcessDataLogger:
    """Check that the logger writes, appends, and clears correctly."""

    def test_record_step_data(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sort_test_step_data: InsertionSortStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right value."""
        logger = insertion_sort_process_data_logger
        step_data = insertion_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)
        step_records: InsertionSortAlgorithmLogDTO = logger.algorithm_log
        expected_index: list[int] = [int(step_data.index)]
        expected_value: list[int] = [int(step_data.value)]
        expected_before: list[tuple[int, ...]] = [step_data.before]
        expected_result: list[tuple[int, ...]] = [step_data.result]
        expected_status: list[str] = [str(step_data.status)]

        assert step_records.index == expected_index
        assert step_records.value == expected_value
        assert step_records.before == expected_before
        assert step_records.result == expected_result
        assert step_records.status == expected_status

    def test_record_step_data_appends(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sort_test_step_data: InsertionSortStepValueObject,
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = insertion_sort_process_data_logger
        step_data = insertion_sort_test_step_data
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_algorithm_log(step_data)

        for field in INSERTION_SORT_EXPECTED_LOG_FIELDS:
            field_len: int = len(getattr(logger.algorithm_log, field))

            assert field_len == test_range

    def test_sort_and_get_process_data(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sorter: InsertionSorter,
    ) -> None:
        """Finished sort ends with READY; log length matches ``iter_steps``."""
        logger = insertion_sort_process_data_logger
        sorter = insertion_sorter
        array: list[int] = INSERTION_SORT_RECORD_TEST_ARRAY.copy()
        process_data: InsertionSortAlgorithmLogDTO = logger.get_result_and_process_data(array)
        end_status: str = process_data.status[-1]
        result_steps_quantity = len(process_data.index)
        expected_steps_quantity = len(list(sorter.iter_steps(INSERTION_SORT_RECORD_TEST_ARRAY)))

        assert end_status == SortingStatus.READY
        assert result_steps_quantity == expected_steps_quantity

    def test_sort_to_clean_previous_log(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
    ) -> None:
        """A second sort must replace the old log, not grow it."""
        logger = insertion_sort_process_data_logger
        first_array: list[int] = INSERTION_SORT_RECORD_TEST_ARRAY.copy()
        second_array: list[int] = INSERTION_SORT_RECORD_TEST_ARRAY.copy()
        first_log: InsertionSortAlgorithmLogDTO = logger.get_result_and_process_data(first_array)
        second_log: InsertionSortAlgorithmLogDTO = logger.get_result_and_process_data(second_array)
        first_log_len = len(first_log.value)
        second_log_len = len(second_log.value)

        assert second_log_len == first_log_len

    def test_get_result_array_from_process_log(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
        insertion_sort_test_step_data: InsertionSortStepValueObject,
    ) -> None:
        """The last recorded array snapshot is the sorted result."""
        logger = insertion_sort_process_data_logger
        step_data = insertion_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)

        array_from_result: tuple[int, ...] = logger.get_result_array_from_process_log()
        expected_result: tuple[int, ...] = step_data.result

        assert array_from_result == expected_result

    def test_get_result_array_from_empty_result(
        self,
        insertion_sort_process_data_logger: InsertionSortProcessDataLogger,
    ) -> None:
        """An empty log must raise ``EmptyResultInProcessLogError``."""
        logger = insertion_sort_process_data_logger

        with pytest.raises(EmptyResultInProcessLogError, match=Messages.EMPTY_RESULT_IN_LOG):
            logger.get_result_array_from_process_log()
