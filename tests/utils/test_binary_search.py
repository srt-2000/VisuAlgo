from collections import defaultdict

import pytest

from pandas import DataFrame
from backend.utils.dataframe import get_dataframe_for_result_table
from backend.utils.constants import DataFrameStr
from tests.utils.cases import DATAFRAME_TEST_INVARIANTS


class TestGetDataFrameForResultTable:

    @pytest.mark.parametrize("test_data", DATAFRAME_TEST_INVARIANTS)
    def test_not_empty_invariants(self, test_data: defaultdict[str, list[str]]) -> None:
        # result dataset
        result_dataframe: DataFrame = get_dataframe_for_result_table(data_for_dataframe=test_data)
        result_rows: int = len(result_dataframe)
        result_index: list[str] = list(result_dataframe.index)
        result_columns: list[str] = list(result_dataframe.columns)

        # expected dataset
        expected_rows: int = len(next(iter(test_data.values())))
        expected_index: list[str] = [
            f"{DataFrameStr.AXIS_NAME} {i}" for i in range(1, expected_rows + 1)
        ]
        expected_columns: list[str] = list(test_data.keys())

        assert not result_dataframe.empty
        assert result_rows == expected_rows
        assert result_index == expected_index
        assert result_columns == expected_columns

        for column, values in test_data.items():
            result_values: list[str] = result_dataframe[column].tolist()

            assert result_values == values