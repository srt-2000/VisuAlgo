"""Labels for quick-sort recursion-tree branches."""

from enum import StrEnum


class RecursionTreeSide(StrEnum):
    """Where the current partition sits in the recursion tree.

    ``ROOT`` is the first call. ``LEFT`` / ``RIGHT`` mark the
    subarrays built from values less / greater than the pivot.
    """

    ROOT = "root"
    LEFT = "left"
    RIGHT = "right"
