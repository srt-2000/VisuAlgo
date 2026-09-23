"""Streamlit page: run binary search and show each step in a table."""

from collections import defaultdict

import streamlit as st
from pandas import DataFrame

from backend.algorithms.binary_search import BinarySearch
from backend.utils.dataframe import get_dataframe_for_result_table
from frontend.element_settings import Icon, PageTitle, SliderLiteral, TableBorderLiteral
from frontend.pages.binary_search.content import PageContent
from frontend.pages.binary_search.element_settings import (
    Header,
    SliderInt,
    SliderStr,
    Badge,
    BadgeColor,
    NumberInputInt,
    NumberInputStr,
    Button,
    Error,
    Success,
)
from backend.services.binary_search import BinarySearchProcessDataLogger
from backend.services.exceptions import TargetIndexNotFoundException


st.set_page_config(page_title=PageTitle.BINARY_SEARCH_ALGORITHM)

st.header(body=Header.BINARY_SEARCH, divider=Header.DIVIDER)
st.markdown(body=PageContent.BINARY_SEARCH_WELCOME)

slider_min_value, slider_max_value = st.slider(
    label=SliderStr.LABEL,
    min_value=SliderInt.MIN,
    max_value=SliderInt.MAX,
    value=(
        SliderInt.START_RENDER_MIN,
        SliderInt.START_RENDER_MAX
    ),
    key=SliderStr.LIST_RANGE_LENGTH,
    bind=SliderLiteral.QUERY_PARAMS,
)

slider_mid_value_render: int = (slider_min_value + slider_max_value) // 2

st.badge(
    label=f"{Badge.SORTED_LIST_LABEL}**[{slider_min_value} ... {slider_max_value}]**",
    color=BadgeColor.GREEN,
)

inputted_target: int = st.number_input(
    label=NumberInputStr.LABEL,
    min_value=slider_min_value,
    max_value=slider_max_value,
    value=slider_mid_value_render,
    step=NumberInputInt.STEP,
    key=NumberInputStr.KEY_INPUTTED_TARGET,
)

if st.button(label=Button.LABEL):
    array_from_slider: list[int] = [
        number for number in range(slider_min_value, slider_max_value + 1)
    ]
    binary_searcher = BinarySearch()
    process_logger = BinarySearchProcessDataLogger(binary_searcher)

    try:
        process_data: defaultdict[str, list[str]] = (
            process_logger.get_result_and_process_data(
                array_from_slider, inputted_target
            )
        )
    except TargetIndexNotFoundException:
        st.error(body=f"{inputted_target} {Error.NOT_FOUND_MESSAGE}")
    else:
        dataframe_for_table: DataFrame = get_dataframe_for_result_table(data_for_dataframe=process_data)
        target_index: str = process_logger.get_target_index_from_process_log()

        st.table(data=dataframe_for_table, border=TableBorderLiteral.HORIZONTAL_BORDER)

        st.success(
            body=f"{inputted_target} {Success.SUCCESS_MESSAGE} **[{target_index}]**",
            icon=Icon.CHECK,
        )

        st.markdown(body=PageContent.RESULT)

        st.balloons()
