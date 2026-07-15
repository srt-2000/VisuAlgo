"""Streamlit page that visualizes binary search and shows per-step logs."""

import streamlit as st
import pandas as pd


from algorithms.binary_search import BinarySearch
from services.binary_search import BinarySearchProcessDataLogger
from services.exceptions import TargetIndexNotFoundException

st.header("BINARY SEARCH", divider="green")
st.markdown(
    """
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
)

slider_min_value, slider_max_value = st.slider(
    label="Define your sorted list range on the slider scale",
    min_value=1,
    max_value=1000,
    value=(300, 800),
    key="list_range",
    bind="query-params",
)
slider_mid_value: int = (slider_min_value + slider_max_value) // 2

st.badge(
    label=(
        "You defined **0-indexed** and sorted list with elements numbers range "
        f"**[{slider_min_value} ... {slider_max_value}]**"
    ),
    color="green",
)

inputted_target = st.number_input(
    label="Input a TARGET number value",
    min_value=slider_min_value,
    max_value=slider_max_value,
    value=slider_mid_value,
    step=1,
    key="inputted_target",
)

if st.button("Find the target number index"):
    array_from_slider: list[int] = [
        number for number in range(slider_min_value, slider_max_value + 1)
    ]
    binary_searcher = BinarySearch()
    process_logger = BinarySearchProcessDataLogger(binary_searcher)

    try:
        process_data = process_logger.search_and_get_process_data(
            array_from_slider, inputted_target
        )
    except TargetIndexNotFoundException:
        st.error(f"Target {inputted_target} not found after algorithm's work")
    else:
        data_frame_for_table = pd.DataFrame(data=process_data)
        data_frame_range: range = range(1, len(data_frame_for_table) + 1)
        data_frame_for_table = data_frame_for_table.set_axis(
            [f"step {i}" for i in data_frame_range], axis=0
        )
        target_index: str = process_data["middle index"][-1]

        st.table(data_frame_for_table, border="horizontal")

        st.success(
            body=f"Target number {inputted_target} has index **[{target_index}]**",
            icon=":material/check:",
        )

        st.markdown(
            """
            ### As you see in every step_data we:
            - Find the middle number of the array
            - And compare it to the target
            - Depends on check status we are changing left_index or right_index search border
            - Every step_data the range size is decreasing
            - We found the target position with :green[**O(log(n))**] time complexity
            """
        )

        st.balloons()
