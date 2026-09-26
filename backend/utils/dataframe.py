from collections import defaultdict
from typing import Iterable

from pandas import DataFrame

from backend.utils.constants import DataFrameStr, DataFrameInt


def get_dataframe_for_result_table(
    data_for_dataframe: defaultdict[str, list[str]],
) -> DataFrame:
    dataframe_for_table = DataFrame(data=data_for_dataframe)
    dataframe_range: Iterable[int] = range(1, len(dataframe_for_table) + 1)

    dataframe_for_table: DataFrame = dataframe_for_table.set_axis(
        labels=[f"{DataFrameStr.AXIS_NAME} {i}" for i in dataframe_range],
        axis=DataFrameInt.AXIS_LINES_CHANGES_PARAMETER,
    )

    return dataframe_for_table
