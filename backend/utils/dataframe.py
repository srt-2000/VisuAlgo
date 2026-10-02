"""Turn an algorithm step log into a pandas table for the UI."""

from collections.abc import Iterable
from typing import Any

import pandas as pd
from backend.domains.base import BaseAlgorithmLogDTO
from backend.utils.constants import DataFrameLiterals


def get_dataframe_for_result_table(
    data_for_dataframe: BaseAlgorithmLogDTO,
) -> pd.DataFrame:
    """Turn a step log into a table with one row per step.

    Column names come from the log fields. Row labels look like
    ``step 1``, ``step 2``, and so on.

    Args:
        data_for_dataframe: Filled algorithm log.

    Returns:
        Table ready to pass to ``st.table``.
    """
    serialized_data: dict[str, list[Any]] = data_for_dataframe.__dict__
    dataframe_for_table = pd.DataFrame(data=serialized_data)
    dataframe_range: Iterable[int] = range(1, len(dataframe_for_table) + 1)

    dataframe_for_table = dataframe_for_table.set_axis(
        labels=[f"{DataFrameLiterals.AXIS_NAME} {i}" for i in dataframe_range],
        axis=DataFrameLiterals.AXIS_LINES_CHANGES_PARAMETER,
    )

    return dataframe_for_table
