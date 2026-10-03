"""Unit tests for ``get_dataframe_for_result_table``."""

from dataclasses import Field, fields
from typing import Any

import pandas as pd
import pytest

from backend.utils.constants import DataFrameLiterals
from backend.utils.dataframe import get_dataframe_for_result_table, get_new_dict_with_removed_under_score_from_keys
from tests.conftest import AlgorithmLogDTO
from tests.utils.cases import UNDERSCORE_REMOVING_DATA_SET


class TestGetDataFrameForResultTable:
    """Check that a filled log becomes a table with the same rows and columns."""

    def test_not_empty(self, algorithm_log_dto: AlgorithmLogDTO) -> None:
        """Row count, labels, column names, and cell values must match the log."""
        # result dataset
        result_dataframe: pd.DataFrame = get_dataframe_for_result_table(data_for_dataframe=algorithm_log_dto)
        result_rows_quantity: int = len(result_dataframe)
        result_index: list[str] = list(result_dataframe.index)
        result_columns: list[str] = list(result_dataframe.columns)

        # expected dataset
        log_fields: tuple[Field[Any], ...] = fields(algorithm_log_dto)
        first_log_field_name: str = log_fields[0].name
        first_log_field_data: list[str] = getattr(algorithm_log_dto, first_log_field_name)
        expected_rows_quantity: int = len(first_log_field_data)
        expected_index: list[str] = [f"{DataFrameLiterals.AXIS_NAME} {i}" for i in range(1, expected_rows_quantity + 1)]
        expected_columns: list[str] = [field.name.replace("_", " ") for field in log_fields]

        assert not result_dataframe.empty
        assert result_rows_quantity == expected_rows_quantity
        assert result_index == expected_index
        assert result_columns == expected_columns

        for field in log_fields:
            result_field_name: str = field.name.replace("_", " ")
            result_values: list[str] = result_dataframe[result_field_name].tolist()
            expected_values: list[str] = getattr(algorithm_log_dto, field.name)

            assert result_values == expected_values


class TestUnderScoreRemoving:
    """Check that underscores disappear from dict keys."""

    @pytest.mark.parametrize("test_dict", UNDERSCORE_REMOVING_DATA_SET)
    def test_remove_under_score_from_keys(self, test_dict: dict[str, Any]) -> None:
        """Keys keep length and values; no key may still contain ``_``."""
        result_array: dict[str, Any] = get_new_dict_with_removed_under_score_from_keys(test_dict)
        expected_array_length: int = len(test_dict)
        result_array_length: int = len(result_array)

        assert expected_array_length == result_array_length

        for key in result_array:
            for letter in key:
                assert letter != "_"
