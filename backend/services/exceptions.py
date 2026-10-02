"""Custom exceptions used by VisuAlgo services."""

from backend.services.constants import Messages


class TargetIndexNotFoundError(Exception):
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
        super().__init__(f"{Messages.TARGET_NUMBER} {target_number} {Messages.INDEX_NOT_FOUND}")


class EmptyResultInProcessLogError(Exception):
    """Raised when code tries to read a step from an empty process log."""

    def __init__(
        self,
    ) -> None:
        """Build the exception with the empty-log message."""
        super().__init__(Messages.EMPTY_RESULT_IN_LOG)
