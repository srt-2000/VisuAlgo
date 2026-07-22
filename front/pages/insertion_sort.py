"""Streamlit page: build a random list and sort it with insertion sort."""

import streamlit as st

from algorithms.insertion_sort import InsertionSorter
from utils.sorting import get_not_sorted_random_list

st.set_page_config(page_title="Insertion Sort Algorithm")

if "not_sorted_array" not in st.session_state:
    st.session_state.not_sorted_array = None
if "sorted_array" not in st.session_state:
    st.session_state.sorted_array = None

st.header("INSERTION SORT", divider="yellow")
st.markdown(
    """
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
)
left, mid, right = st.columns(3)

not_sorted_list_length: int = left.number_input(
    icon=":material/input:",
    label="length",
    placeholder="Enter a number",
    min_value=0,
    max_value=50,
    value=3,
    step=1,
)

min_value_limit: int = mid.number_input(
    icon=":material/input:",
    label="minimum value",
    placeholder="Enter a number",
    min_value=-100,
    max_value=100,
    value=-90,
    step=1,
)

max_value_limit: int = right.number_input(
    icon=":material/input:",
    label="maximum value",
    placeholder="Enter a number",
    min_value=min_value_limit,
    max_value=100,
    value=90,
    step=1,
)

not_sorted_column, sorted_column = st.columns(2, border=True)

if not_sorted_list_length and min_value_limit and max_value_limit:
    if not_sorted_column.button("CREATE"):
        st.session_state.not_sorted_array = get_not_sorted_random_list(
            not_sorted_list_length,
            min_value_limit,
            max_value_limit,
        )
        st.session_state.sorted_array = None

if st.session_state.not_sorted_array is not None:
    if sorted_column.button("SORT IT"):
        sorter: InsertionSorter = InsertionSorter()
        array: list[int] = st.session_state.not_sorted_array.copy()
        sorted_array: list[int] = sorter.sort(array)
        st.session_state.sorted_array = sorted_array

if st.session_state.not_sorted_array is not None:
    not_sorted_column.info(":material/done_outline:NOT sorted array")
    not_sorted_column.write(st.session_state.not_sorted_array)

if st.session_state.sorted_array is not None:
    sorted_column.success(":material/done_outline:Sorted array")
    sorted_column.write(st.session_state.sorted_array)
