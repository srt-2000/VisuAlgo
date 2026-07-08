"""Core binary search implementation used across the application."""

from loguru import logger


class ElementPositionFinder:
    """Searches for element positions in sorted integer sequences."""

    def __init__(self) -> None:
        """Initialize internal index boundaries for the search process."""
        self.max_index: int = 0
        self.min_index: int = 0

    def binary_search(self, sequence: list[int], target_element: int) -> int | None:
        """Perform an iterative binary search on a sorted sequence.

        Args:
            sequence: Sorted list of integers to search in.
            target_element: Target integer value to look up.

        Returns:
            Index of the target element in the sequence if found, otherwise ``None``.
        """
        self.max_index = len(sequence) - 1

        while self.min_index <= self.max_index:
            mid_index: int = (self.min_index + self.max_index) // 2
            checking_element: int = sequence[mid_index]
            logger.info("Trying index range %s ... %s", self.min_index, self.max_index)

            if checking_element == target_element:
                return mid_index
            if checking_element > target_element:
                self.max_index = mid_index - 1
            else:
                self.min_index = mid_index + 1
        logger.warning("Target index not found")
        return None
