"""Domain and service exceptions for VisuAlgo."""

from services.constants import Messages


class TargetIndexNotFoundException(Exception):
    """Raised when binary search cannot locate the requested target.

    Attributes:
        target_number: Target value that was not found.
    """

    def __init__(self, target_number: int) -> None:
        """Build the exception with a descriptive message.

        Args:
            target_number: Target value that was not found in the array.
        """
        self.target_number: int = target_number
        super().__init__(
            f"{Messages.TARGET_NUMBER} {target_number} {Messages.INDEX_NOT_FOUND}"
        )
