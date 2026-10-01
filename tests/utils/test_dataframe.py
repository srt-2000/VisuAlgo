from dataclasses import fields, Field
from typing import Any

from pandas import DataFrame

from backend.utils.constants import DataFrameLiterals
from backend.utils.dataframe import get_dataframe_for_result_table
from tests.conftest import AlgorithmLogDTO


class TestGetDataFrameForResultTable:
    def test_not_empty(
            self,
            log_dto: AlgorithmLogDTO
    ) -> None:
        # result dataset
        result_dataframe: DataFrame = get_dataframe_for_result_table(
            data_for_dataframe=log_dto
        )
        result_rows_quantity: int = len(result_dataframe)
        result_index: list[str] = list(result_dataframe.index)
        result_columns: list[str] = list(result_dataframe.columns)

        # expected dataset
        log_fields: tuple[Field[Any],...] = fields(log_dto)
        first_log_field_name: str = log_fields[0].name
        first_log_field_data: list[str] = getattr(log_dto, first_log_field_name)
        expected_rows_quantity: int = len(first_log_field_data)
        expected_index: list[str] = [
            f"{DataFrameLiterals.AXIS_NAME} {i}" for i in range(1, expected_rows_quantity + 1)
        ]
        expected_columns: list[str] = [field.name for field in log_fields]

        assert not result_dataframe.empty
        assert result_rows_quantity == expected_rows_quantity
        assert result_index == expected_index
        assert result_columns == expected_columns

        for field in log_fields:
            result_values: list[str] = result_dataframe[field.name].tolist()
            expected_values: list[str] = getattr(log_dto, field.name)

            assert result_values == expected_values
