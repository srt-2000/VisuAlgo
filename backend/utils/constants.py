"""Labels used when a step log becomes a pandas table."""

from typing import Literal


class DataFrameLiterals:
    """Pieces of the row-label text on the steps table.

    Attributes:
        AXIS_NAME: Prefix, so rows are named ``step 1``, ``step 2``.
        AXIS_LINES_CHANGES_PARAMETER: Pandas axis that those row labels sit on.
    """

    AXIS_NAME: Literal["step"] = "step"
    AXIS_LINES_CHANGES_PARAMETER: Literal["index"] = "index"
