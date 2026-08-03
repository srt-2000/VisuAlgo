"""Start VisuAlgo: wire Streamlit navigation to the app pages."""

import streamlit as st
from streamlit.navigation.page import StreamlitPage

from front.components.pages_container import PagesContainer

pages: list[StreamlitPage] = PagesContainer.get_pages()
app_start_page: StreamlitPage = st.navigation(pages)

if __name__ == "__main__":
    app_start_page.run()
