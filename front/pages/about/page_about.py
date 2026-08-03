"""About page: what VisuAlgo is and how to start."""

import streamlit as st

from front.element_settings import PageTitle
from front.pages.about.element_settings import Header
from front.pages.about.content import PageContent

st.set_page_config(page_title=PageTitle.ABOUT)

st.header(
    body=Header.WELCOME_MESSAGE,
    divider=Header.DIVIDER,
    help=Header.HELP_INFO,
)
st.markdown(PageContent.WELCOME_CONTENT)
