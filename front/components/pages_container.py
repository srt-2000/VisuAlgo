"""Holds Streamlit pages used in the app sidebar navigation."""

import streamlit
from streamlit.navigation.page import StreamlitPage


class PagesContainer:
    """Collect every ``StreamlitPage`` defined on this class."""

    main: StreamlitPage = streamlit.Page(
        page="front/pages/about.py",
        title="About",
        icon=":material/info:",
    )

    binary_search: StreamlitPage = streamlit.Page(
        page="front/pages/binary_search.py",
        title="Binary Search Algorithm",
        icon=":material/search_check_2:",
    )

    insertion_sort: StreamlitPage = streamlit.Page(
        page="front/pages/insertion_sort.py",
        title="Insertion Sort Algorithm",
        icon=":material/sort:",
    )

    @classmethod
    def get_pages(cls) -> list[StreamlitPage]:
        """Return all page objects registered on this class.

        Returns:
            Pages ready for Streamlit navigation.
        """
        pages: list[StreamlitPage] = []

        for page in cls.__dict__.values():
            if not callable(page) and isinstance(page, StreamlitPage):
                pages.append(page)
        return pages
