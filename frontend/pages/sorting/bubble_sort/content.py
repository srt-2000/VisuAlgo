"""Markdown body text for the bubble-sort page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks: how bubble sort works and what the result means."""

    BUBBLE_SORT_WELCOME = """
    ### Complexity:
    - Time Complexity:
        - :violet[**O(n²)**] if array is already completely sorted for classic algorithm (:green[**our case**])
        - :violet[**O(n)**] if array is already completely sorted for early-exit configuration (:red[**not classic**])
        - :violet[**O(n²)**] if elements are scattered randomly
        - :violet[**O(n²)**] if array is sorted in exact reverse order
    - Space Complexity: :violet[**O(1)**] because modifies the array in-place
    ### How does it work:
    - Simple and :green[**stable**], but slow: fine only for :red[tiny / teaching] arrays, not for production
    - Start from the left of the array
    - Compare each pair of :green[**adjacent**] elements
    - If they are out of order — :red[**swap**] them
    - After one full pass the :green[**largest**] element
    "bubbles up" to the end of the unsorted section
    - Shrink the unsorted range by one (the rightmost part is sorted)
    - Repeat passes until no swaps are needed
      or the unsorted section is empty

    ### Try to use:
    - First of all let's create a not sorted random array
    """

    RESULT = """
        ### As you see in every step we:
        - Compare a pair of adjacent elements
        - Swap them if they are out of order
        - After each pass the largest unsorted value
          settles at the end of the unsorted section
        - Shrink the unsorted range and continue
        """
