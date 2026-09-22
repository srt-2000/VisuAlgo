"""Custom exceptions used by VisuAlgo services."""

from backend.services.constants import Messages


class TargetIndexNotFoundException(Exception):
    """Raised when the target number is not in the list.

    Attributes:
        target_number: The missing target value.
    """

    def __init__(self, target_number: int) -> None:
        """Build an exception that names the missing target.

        Args:
            target_number: Value that was not found.
        """
        self.target_number: int = target_number
        super().__init__(
            f"{Messages.TARGET_NUMBER} {target_number} {Messages.INDEX_NOT_FOUND}"
        )


class EmptyResultInProcessLog(Exception):
    """Raised when the target index value is empty after algorithm got result."""

    def __init__(self,) -> None:
        """Build an exception that write the problem."""
        super().__init__(Messages.EMPTY_RESULT_IN_LOG)
