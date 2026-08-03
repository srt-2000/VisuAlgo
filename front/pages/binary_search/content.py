"""Markdown body text for the binary-search page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks: how binary search works and what the result means."""

    BINARY_SEARCH_WELCOME = """
    ### Complexity:
    - Time Complexity: :green[**O(log(n))**]
    - Space Complexity: :green[**O(1)**]
    ### How does it work: 
    - For :red[**SORTED**] arrays only
    - Find the middle number of the array
    - Compare the middle number with the target key. 
        - If equal: return index
        - If the key is smaller: search the left_index half
        - If the key is larger: search the right_index half
    - Repeat until the number is found or the search space is empty
    ### Try to use:
    - In our case we use a **while loop** - efficient in both time and space
    """

    RESULT = """
            ### As you see in every step_data we:
            - Find the middle number of the array
            - And compare it to the target
            - Depends on check status we are changing left_index or right_index search border
            - In every step the range size is decreasing
            - We found the target position with :green[**O(log(n))**] time complexity
            """
