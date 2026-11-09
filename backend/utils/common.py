"""Small generic helpers used across algorithm pages."""

from itertools import chain
from typing import Any


def unpack_sublists_to_array(array_with_sublists: tuple[list[int], ...]) -> tuple[int, ...]:
    """Flatten nested int lists into one flat tuple.

    Quick-sort logs store each step as ``(left, middle, right)``. This
    helper stitches those buckets back into one sequence for the UI.

    Args:
        array_with_sublists: Tuple of int lists to concatenate in order.

    Returns:
        One flat tuple with every element from every sublist.
    """
    chain_link: chain[Any] = chain.from_iterable(array_with_sublists)
    unpacked_result: tuple[int, ...] = tuple(chain_link)

    return unpacked_result
