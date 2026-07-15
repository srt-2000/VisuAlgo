"""Binary search algorithm over sorted integer arrays."""

from typing import Iterator

from domains.binary_search import BinarySearchStepValueObject, BinarySearchStatus


class BinarySearch:
    """Binary search over a sorted integer array.

    Provides both a direct index lookup and a step-by-step iterator used for
    visualization of the search process.
    """

    def search(self, array: list[int], target: int) -> int | None:
        """Return the index of ``target`` in a sorted ``array``.

        Args:
            array: Sorted list of integers to search.
            target: Value to locate.

        Returns:
            Zero-based index of ``target`` if present, otherwise ``None``.
        """
        for step in self.iter_steps(array, target):
            if step.status == BinarySearchStatus.EQUAL:
                return step.mid_index
        return None

    @staticmethod
    def iter_steps(
        array: list[int],
        target: int,
    ) -> Iterator[BinarySearchStepValueObject]:
        """Yield one step per mid-element comparison.

        Each yielded value describes the current search window and the outcome
        of comparing ``array[mid]`` with ``target``. The generator stops after
        an equality match or when the search window becomes empty.

        Args:
            array: Sorted list of integers to search.
            target: Value to locate.

        Yields:
            Immutable step snapshot for visualization and logging.
        """
        left_index: int = 0
        right_index: int = len(array) - 1

        while left_index <= right_index:
            mid_index: int = (left_index + right_index) // 2
            mid_value: int = array[mid_index]

            if mid_value == target:
                yield BinarySearchStepValueObject(
                    left_index,
                    right_index,
                    mid_index,
                    mid_value,
                    BinarySearchStatus.EQUAL,
                    target,
                )
                return
            if mid_value > target:
                yield BinarySearchStepValueObject(
                    left_index,
                    right_index,
                    mid_index,
                    mid_value,
                    BinarySearchStatus.GREATER,
                    target,
                )
                right_index = mid_index - 1
            else:
                yield BinarySearchStepValueObject(
                    left_index,
                    right_index,
                    mid_index,
                    mid_value,
                    BinarySearchStatus.LESS,
                    target,
                )
                left_index = mid_index + 1
