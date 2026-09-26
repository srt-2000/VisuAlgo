"""Streamlit page: build a random list and sort it with insertion sort."""

from collections import defaultdict

import streamlit as st


from backend.algorithms.insertion_sort import InsertionSorter
from backend.utils.dataframe import get_dataframe_for_result_table
from frontend.element_settings import PageTitle, Icon, SliderLiteral, TableBorderLiteral
from frontend.pages.insertion_sort.constants import Fields, Messages
from frontend.pages.insertion_sort.content import PageContent
from frontend.pages.insertion_sort.element_settings import (
    Header,
    NumberInputStr,
    LeftColumnNumberInputInt,
    Columns,
    Button,
    RightColumnSliderInt,
    RightColumnSliderStr,
)
from backend.services.insertion_sort import InsertionSortProcessDataLogger
from backend.utils.sorting import get_not_sorted_random_list

st.set_page_config(page_title=PageTitle.INSERTION_SORT_ALGORITHM)

if Fields.NOT_SORTED_ARRAY not in st.session_state:
    st.session_state.not_sorted_array = None
if Fields.SORTED_ARRAY not in st.session_state:
    st.session_state.sorted_array = None
if Fields.PROCESS_DATA not in st.session_state:
    st.session_state.process_data = None


st.header(body=Header.INSERTION_SORT, divider=Header.DIVIDER)

st.markdown(body=PageContent.INSERTION_SORT_WELCOME)

left_column, right_column = st.columns(spec=Columns.RANDOM_LIST_DATA_COLUMNS_QUANTITY)

not_sorted_list_length: int = left_column.number_input(
    icon=Icon.INPUT,
    label=NumberInputStr.LABEL_LENGTH,
    placeholder=NumberInputStr.PLACEHOLDER_ENTER_NUMBER,
    min_value=LeftColumnNumberInputInt.MIN,
    max_value=LeftColumnNumberInputInt.MAX,
    value=LeftColumnNumberInputInt.RENDER,
    step=LeftColumnNumberInputInt.STEP,
)

randomizer_min_value, randomizer_max_value = right_column.slider(
    label=RightColumnSliderStr.LABEL,
    min_value=RightColumnSliderInt.MIN,
    max_value=RightColumnSliderInt.MAX,
    value=(
        RightColumnSliderInt.MIN_RENDER,
        RightColumnSliderInt.MAX_RENDER,
    ),
    key=RightColumnSliderStr.KEY,
    bind=SliderLiteral.QUERY_PARAMS,
)

not_sorted_column, sorted_column = st.columns(
    spec=Columns.LIST_RENDER_COLUMNS_QUANTITY, border=True
)

if not_sorted_column.button(label=Button.LABEL_CREATE):
    st.session_state.not_sorted_array = get_not_sorted_random_list(
        not_sorted_list_length,
        randomizer_min_value,
        randomizer_max_value,
    )
    st.session_state.sorted_array = None

if st.session_state.not_sorted_array is not None:
    not_sorted_column.info(body=Messages.NOT_SORTED_ARRAY, icon=Icon.DONE_OUTLINE)
    not_sorted_column.write(tuple(st.session_state.not_sorted_array))

    if sorted_column.button(label=Button.LABEL_SORT_IT):
        array: list[int] = st.session_state.not_sorted_array.copy()
        sorter = InsertionSorter()
        process_logger = InsertionSortProcessDataLogger(sorter)
        process_data: defaultdict[str, list[int | str | tuple[int, ...]]] = (
            process_logger.get_result_and_process_data(
                st.session_state.not_sorted_array
            )
        )

        sorted_array: tuple[int, ...] = (
            process_logger.get_result_array_from_process_log()
        )

        st.session_state.not_sorted_array = array
        st.session_state.sorted_array = sorted_array
        st.session_state.process_data = process_data

        st.snow()

if (st.session_state.sorted_array and st.session_state.process_data) is not None:
    sorted_column.success(body=Messages.SORTED_ARRAY, icon=Icon.DONE_OUTLINE)
    sorted_column.write(st.session_state.sorted_array)

    data_frame_for_table = get_dataframe_for_result_table(
        data_for_dataframe=st.session_state.process_data
    )

    st.table(data=data_frame_for_table, border=TableBorderLiteral.HORIZONTAL_BORDER)

    st.markdown(PageContent.RESULT)
