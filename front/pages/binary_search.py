"""Streamlit page that visualizes and explains the binary search algorithm."""

import streamlit as st

from src.binary_search import ElementPositionFinder

st.title("BINARY SEARCH")
st.markdown(
    """
    This algorithm can quickly find a target element position in a sequence.
    The sequence must be sorted and iterable.

    ### Complexity:
    - Time Complexity: **O(log(n))**
    - Space Complexity: **O(1)**

    ### How does it work:
    - Find the middle element of the array
    - Compare the middle element with the target key. If equal: return index
    - If the key is smaller: search the left half
    - If the key is larger: search the right half
    - Repeat until the element is found or the search space is empty

    ### Try to use:
    - In our case we use a **while loop** - efficient in both time and space
    """,
)

min_value, max_value = st.slider(
    label="Define your sorted list range on the slider scale",
    min_value=0,
    max_value=1000,
    value=(300, 800),
    key="list_range",
    bind="query-params",
)
mid_value: int = (min_value + max_value) // 2

st.badge(
    label=(
        "You defined **0-indexed** and sorted list with elements numbers range "
        f"**[{min_value} ... {max_value}]**"
    ),
    color="green",
)

target_element = st.number_input(
    label="Input a TARGET element number",
    min_value=min_value,
    max_value=max_value,
    value=mid_value,
    step=1,
    key="target_number",
)

if st.button("Find the target element index"):
    finder: ElementPositionFinder = ElementPositionFinder()
    range_list: list[int] = [element for element in range(min_value, max_value)]
    result: int | None = finder.binary_search(range_list, target_element)

    if result is not None:
        st.success(
            body=f"Target element index is **{result}**",
            icon=":material/check:",
        )
    else:
        st.error(
            body="Target element index is **not found**, check logger output.",
            icon=":material/check:",
        )
