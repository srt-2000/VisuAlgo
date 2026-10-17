"""Unit tests for ``SelectionSortProcessDataLogger``."""

import pytest

from backend.domains.constants import SortingStatus
from backend.domains.sorting import BaseSortAlgorithmLogDTO, BaseSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError
from backend.services.sorting.selection import SelectionSortProcessDataLogger
from tests.services.sorting.cases import SORT_RECORD_TEST_ARRAY


class TestSelectionSortProcessDataLogger:
    """Check that the logger writes, appends, and clears correctly."""

    def test_record_step_data(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
        selection_sort_test_step_data: BaseSortStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right value."""
        logger = selection_sort_process_data_logger
        step_data = selection_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)
        step_records: BaseSortAlgorithmLogDTO = logger.algorithm_log

        expected_index: list[int] = [step_data.index]
        expected_value: list[int] = [step_data.value]
        expected_before: list[tuple[int, ...]] = [step_data.before]
        expected_result: list[tuple[int, ...]] = [step_data.result]
        expected_status: list[str] = [step_data.status]

        assert step_records.index == expected_index
        assert step_records.value == expected_value
        assert step_records.before == expected_before
        assert step_records.result == expected_result
        assert step_records.status == expected_status

    def test_record_step_data_appends(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
        selection_sort_test_step_data: BaseSortStepValueObject,
        expected_log_fields: tuple[str, ...],
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = selection_sort_process_data_logger
        step_data = selection_sort_test_step_data
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_algorithm_log(step_data)

        for field in expected_log_fields:
            field_len: int = len(getattr(logger.algorithm_log, field))

            assert field_len == test_range

    def test_get_result_and_process_data(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
    ) -> None:
        """Finished sort ends with READY; log length matches comparison count."""
        logger = selection_sort_process_data_logger
        array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        process_data: BaseSortAlgorithmLogDTO = logger.get_result_and_process_data(array)
        end_status: str = process_data.status[-1]
        result_steps_quantity = len(process_data.index)
        expected_steps_quantity: int = len(array) - 1

        assert result_steps_quantity == expected_steps_quantity
        assert end_status == SortingStatus.READY

    def test_sort_to_clean_previous_log(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
    ) -> None:
        """A second sort must replace the old log, not grow it."""
        logger = selection_sort_process_data_logger
        first_array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        second_array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        first_log: BaseSortAlgorithmLogDTO = logger.get_result_and_process_data(first_array)
        second_log: BaseSortAlgorithmLogDTO = logger.get_result_and_process_data(second_array)
        first_log_len = len(first_log.value)
        second_log_len = len(second_log.value)

        assert second_log_len == first_log_len

    def test_get_result_array_from_process_log(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
        selection_sort_test_step_data: BaseSortStepValueObject,
    ) -> None:
        """The last recorded array snapshot is the sorted result."""
        logger = selection_sort_process_data_logger
        step_data = selection_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)

        array_from_result: tuple[int, ...] = logger.get_result_array_from_process_log()
        expected_result: tuple[int, ...] = step_data.result

        assert array_from_result == expected_result

    def test_get_result_array_from_empty_result(
        self,
        selection_sort_process_data_logger: SelectionSortProcessDataLogger,
    ) -> None:
        """An empty log must raise ``EmptyResultInProcessLogError``."""
        logger = selection_sort_process_data_logger

        with pytest.raises(EmptyResultInProcessLogError, match=Messages.EMPTY_RESULT_IN_LOG):
            logger.get_result_array_from_process_log()
