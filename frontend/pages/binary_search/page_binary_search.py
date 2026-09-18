"""Streamlit page: run binary search and show each step in a table."""

from collections import defaultdict
from typing import Iterable

import streamlit as st
import pandas as pd
from pandas import DataFrame

from backend.algorithms.binary_search import BinarySearch
from frontend.element_settings import Icon
from frontend.pages.binary_search.constants import Field
from frontend.pages.binary_search.content import PageContent
from frontend.pages.binary_search.element_settings import (
    PageTitle,
    Header,
    SliderInt,
    SliderStr,
    SliderLiteral,
    Badge,
    BadgeColor,
    NumberInputInt,
    NumberInputStr,
    Button,
    Error,
    TableBorder,
    Success,
    DataFrameInt,
    DataFrameStr,
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
        data_frame_for_table = pd.DataFrame(data=process_data)
        data_frame_range: Iterable[int] = range(1, len(data_frame_for_table) + 1)
        data_frame_for_table: DataFrame = data_frame_for_table.set_axis(
            labels=[f"{DataFrameStr.AXIS_NAME} {i}" for i in data_frame_range],
            axis=DataFrameInt.AXIS_LINES_CHANGES_PARAMETER,
        )
        target_index: str = process_data[Field.MIDDLE_INDEX][-1]

        st.table(data=data_frame_for_table, border=TableBorder.HORIZONTAL_BORDER)

        st.success(
            body=f"{inputted_target} {Success.SUCCESS_MESSAGE} **[{target_index}]**",
            icon=Icon.CHECK,
        )

        st.markdown(body=PageContent.RESULT)

        st.balloons()
