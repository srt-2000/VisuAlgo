"""Markdown body text for the quick-sort page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks: how quick sort works and what the result means."""

    QUICK_SORT_WELCOME = """
    ### Complexity:
    - Time Complexity:
        - :blue[**O(n log n)**] if elements are scattered randomly
          (:green[**average / expected**])
        - :blue[**O(n log n)**] best case — balanced partitions
        - :blue[**O(n²)**] if every partition is heavily unbalanced
          (e.g. already sorted / reverse-sorted with a fixed end pivot)
    - Space Complexity: :blue[**O(log n)**] on average for the recursion stack
      (:green[**in-place partition**]); up to :red[**O(n)**] in the worst case
    ### How does it work:
    - Fast in practice and :red[**unstable**]; the workhorse for
      :green[**large**] arrays, not only for teaching demos
    - Pick a :green[**pivot**] element (first, last, middle, or random —
      strategy varies)
    - :red[**Partition**] the array so that:
      all elements :green[**left**] of the pivot are smaller,
      all elements :green[**right**] are larger
    - The pivot is now in its :green[**final sorted position**]
    - Recursively apply the same process to the left and right subarrays
    - Base cases: empty / single-element subarrays are already sorted

    ### Try to use:
    - First of all let's create a not sorted random array
    """

    RESULT = """
        ### As you see in every step we:
        - Pick a pivot element
        - Partition: smaller values go left, larger go right
        - Pivot settles into its final sorted position
        - Recursively sort the left and right subarrays
        """
