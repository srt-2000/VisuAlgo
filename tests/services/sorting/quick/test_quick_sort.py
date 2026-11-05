"""Unit tests for ``QuickSortProcessDataLogger``."""

import pytest

from backend.domains.constants import SortingStatus
from backend.domains.sorting import QuickSortAlgorithmLogDTO, QuickSortStepValueObject
from backend.services.constants import Messages
from backend.services.exceptions import EmptyResultInProcessLogError
from backend.services.sorting.quick import QuickSortProcessDataLogger
from tests.services.sorting.cases import SORT_RECORD_TEST_ARRAY


class TestQuickSortProcessDataLogger:
    """Check that the logger writes, appends, and clears correctly."""

    def test_record_step_data(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
        quick_sort_test_step_data: QuickSortStepValueObject,
    ) -> None:
        """One recorded step must fill every log field with the right value."""
        logger = quick_sort_process_data_logger
        step_data = quick_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)
        step_records: QuickSortAlgorithmLogDTO = logger.algorithm_log

        expected_depth: list[int] = [step_data.depth]
        expected_side: list[str] = [step_data.side]
        expected_pivot: list[int] = [step_data.pivot]
        expected_before: list[tuple[int, ...]] = [step_data.before]
        expected_result: list[tuple[list[int], ...]] = [step_data.result]
        expected_status: list[str] = [step_data.status]

        assert step_records.depth == expected_depth
        assert step_records.side == expected_side
        assert step_records.pivot == expected_pivot
        assert step_records.before == expected_before
        assert step_records.result == expected_result
        assert step_records.status == expected_status

    def test_record_step_data_appends(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
        quick_sort_test_step_data: QuickSortStepValueObject,
        expected_quick_sort_log_fields: tuple[str, ...],
    ) -> None:
        """Two records must append values, not overwrite earlier ones."""
        logger = quick_sort_process_data_logger
        step_data = quick_sort_test_step_data
        test_range: int = 2

        for _ in range(test_range):
            logger._record_step_data_to_algorithm_log(step_data)

        for field in expected_quick_sort_log_fields:
            field_len: int = len(getattr(logger.algorithm_log, field))

            assert field_len == test_range

    def test_get_result_and_process_data(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
    ) -> None:
        """Finished sort ends with READY."""
        logger = quick_sort_process_data_logger
        array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        process_data: QuickSortAlgorithmLogDTO = logger.get_result_and_process_data(array)
        end_status: str = process_data.status[-1]

        assert end_status == SortingStatus.READY

    def test_sort_to_clean_previous_log(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
    ) -> None:
        """A second sort must replace the old log, not grow it."""
        logger = quick_sort_process_data_logger
        first_array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        second_array: list[int] = SORT_RECORD_TEST_ARRAY.copy()
        first_log: QuickSortAlgorithmLogDTO = logger.get_result_and_process_data(first_array)
        second_log: QuickSortAlgorithmLogDTO = logger.get_result_and_process_data(second_array)
        first_log_len = len(first_log.depth)
        second_log_len = len(second_log.depth)

        assert second_log_len == first_log_len

    def test_get_result_array_from_process_log(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
        quick_sort_test_step_data: QuickSortStepValueObject,
    ) -> None:
        """The last recorded partition snapshot is what this method returns."""
        logger = quick_sort_process_data_logger
        step_data = quick_sort_test_step_data
        logger._record_step_data_to_algorithm_log(step_data)

        array_from_result: tuple[list[int], ...] = logger.get_result_array_from_process_log()
        expected_result: tuple[list[int], ...] = step_data.result

        assert array_from_result == expected_result

    def test_get_result_array_from_empty_result(
        self,
        quick_sort_process_data_logger: QuickSortProcessDataLogger,
    ) -> None:
        """An empty log must raise ``EmptyResultInProcessLogError``."""
        logger = quick_sort_process_data_logger

        with pytest.raises(EmptyResultInProcessLogError, match=Messages.EMPTY_RESULT_IN_LOG):
            logger.get_result_array_from_process_log()
