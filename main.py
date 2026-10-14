"""Start VisuAlgo: wire Streamlit navigation to the app pages."""

import streamlit as st
from streamlit.navigation.page import StreamlitPage

from frontend.navigation.navigation_fabric import get_pages_container

pages: dict[str, list[StreamlitPage]] = get_pages_container()
app_start_page: StreamlitPage = st.navigation(pages)

if __name__ == "__main__":
    app_start_page.run()
