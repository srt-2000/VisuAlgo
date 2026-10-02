"""Binary search over a sorted list of ints."""

from collections.abc import Iterator

from backend.domains.binary_search import BinarySearchStepValueObject
from backend.domains.constants import BinarySearchStatus


class BinarySearch:
    """Find a number in a sorted list by cutting the list in half each time."""

    @staticmethod
    def iter_steps(
        array: list[int],
        target: int,
    ) -> Iterator[BinarySearchStepValueObject]:
        """Yield each guess until ``target`` is found or the window is empty.

        An empty list yields nothing: there is no middle element to check.
        If ``target`` is missing, the generator simply ends. The last step
        is then not an equal hit.

        Args:
            array: Sorted list of ints. Unsorted input gives wrong guesses.
            target: Number to find.

        Yields:
            One snapshot each time the middle element is compared.
        """
        left_index: int = 0
        right_index: int = len(array) - 1

        while left_index <= right_index:
            mid_index: int = (left_index + right_index) // 2
            mid_value: int = array[mid_index]
            left_value: int = array[left_index]
            right_value: int = array[right_index]

            if mid_value == target:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    left_value=left_value,
                    right_index=right_index,
                    right_value=right_value,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.EQUAL,
                    target=target,
                )
                return
            if mid_value > target:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    left_value=left_value,
                    right_index=right_index,
                    right_value=right_value,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.GREATER,
                    target=target,
                )
                right_index = mid_index - 1
            else:
                yield BinarySearchStepValueObject(
                    left_index=left_index,
                    left_value=left_value,
                    right_index=right_index,
                    right_value=right_value,
                    mid_index=mid_index,
                    middle_value=mid_value,
                    status=BinarySearchStatus.LESS,
                    target=target,
                )
                left_index = mid_index + 1
