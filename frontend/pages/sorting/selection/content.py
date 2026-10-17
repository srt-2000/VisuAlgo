"""Markdown body text for the selection-sort page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks: how selection sort works and what the result means."""

    SELECTION_SORT_WELCOME = """
    ### Complexity:
    - Time Complexity:
        - :orange[**O(n²)**] if array is already completely sorted
        - :orange[**O(n²)**] if elements are scattered randomly
        - :orange[**O(n²)**] if array is sorted in exact reverse order
    - Space Complexity: :orange[**O(1)**] because modifies the array in-place
    ### How does it work:
    - Simple and :red[**unstable**], but makes few swaps: fine for :red[tiny / teaching]
    arrays, not for production
    - Treat the left part of the array as the :green[**sorted**] section
    (starts empty)
    - Scan the :green[**unsorted**] section and find the :green[**minimum**] element
    - :red[**Swap**] that minimum with the first element of the unsorted section
    - Grow the sorted section by one position from the left
    - Repeat until the unsorted section is empty

    ### Try to use:
    - First of all let's create a not sorted random array
    """

    RESULT = """
        ### As you see in every step we:
        - Find the minimum in the RIGHT unsorted section
        - Swap it with the first unsorted element
        - Grow the LEFT sorted section by one
        - Continue until the whole array is sorted
        """
