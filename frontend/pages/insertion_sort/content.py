"""Markdown body text for the insertion-sort page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks: how insertion sort works and what the result means."""

    INSERTION_SORT_WELCOME = """
    ### Complexity:
    - Time Complexity:
        - :yellow[**O(n)**] if array is already completely sorted
        - :yellow[**O(n²)**] if elements are scattered randomly
        - :yellow[**O(n²)**] if array is sorted in exact reverse order
    - Space Complexity: :yellow[**O(1)**] because modifies the array in-place
    
    ### How does it work: 
    - In practice this algorithm give a good metrics with sequences with 
    :red[no more 50 elements]
    - Assume the first element is sorted
    - Pick the next element, which becomes the ":green[**key**]"
    - Compare the :green[**key**] with the elements in the sorted section 
    (:red[moving from right to left])
    - Shift all larger elements in the sorted section one position 
    to the right to clear a path
    - Insert the key into its correct placeholder slot
    - Repeat the process for all remaining unsorted items

    ### Try to use:
    - First of all let's create a not sorted random array
    """

    RESULT = """
        ### As you see in every step we:
        - Pick the next element
        - Compare it with the elements in the LEFT sorted section 
        - Shift all larger elements in the sorted section 
        - Insert element into its correct position
        """
