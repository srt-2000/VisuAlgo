"""Binary search over a sorted list of ints."""

from typing import Iterator

from backend.algorithms.interfaces import AlgorithmBase
from backend.domains.binary_search import BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus


class BinarySearch(AlgorithmBase):
    """Find a number in a sorted list by cutting the list in half each time."""

    def search(self, array: list[int], target: int) -> int | None:
        """Return the index of ``target``, or ``None`` if it is missing.

        Args:
            array: Sorted list of ints.
            target: Number to find.

        Returns:
            Index of ``target``, or ``None`` when it is not in ``array``.
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
        """Yield each guess until we find ``target`` or run out of room.

        Args:
            array: Sorted list of ints.
            target: Number to find.

        Yields:
            One step snapshot per middle-element check.
        """
        left_index: int = 0
        right_index: int = len(array) - 1

        while left_index <= right_index:
            mid_index: int = (left_index + right_index) // 2
            mid_value: int = array[mid_index]

            if mid_value == target:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    right_index=right_index,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.EQUAL,
                    target=target,
                )
                return
            if mid_value > target:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    right_index=right_index,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.GREATER,
                    target=target,
                )
                right_index = mid_index - 1
            else:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    right_index=right_index,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.LESS,
                    target=target,
                )
                left_index = mid_index + 1
