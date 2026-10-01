from collections.abc import Iterable
from typing import Any

from pandas import DataFrame

from backend.domains.base import BaseAlgorithmLogDTO
from backend.utils.constants import DataFrameLiterals


def get_dataframe_for_result_table(
    data_for_dataframe: BaseAlgorithmLogDTO,
) -> DataFrame:
    """Formatting the BaseAlgorithmLogDTO to DataFrame object.
        Args:
            data_for_dataframe: Data from process log.
        Returns: Dataframe object.
        """
    serialized_data: dict[str, list[Any]] = data_for_dataframe.__dict__
    dataframe_for_table = DataFrame(data=serialized_data)
    dataframe_range: Iterable[int] = range(1, len(dataframe_for_table) + 1)

    dataframe_for_table = dataframe_for_table.set_axis(
        labels=[f"{DataFrameLiterals.AXIS_NAME} {i}" for i in dataframe_range],
        axis=DataFrameLiterals.AXIS_LINES_CHANGES_PARAMETER,
    )

    return dataframe_for_table
