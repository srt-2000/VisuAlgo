"""Holds Streamlit pages used in the app sidebar navigation."""

import streamlit
from streamlit.navigation.page import StreamlitPage

from front.components.element_settings import LeftNavigationTitle, PagePath
from front.element_settings import Icon


class PagesContainer:
    """Holds every ``StreamlitPage`` wired into the sidebar."""

    main: StreamlitPage = streamlit.Page(
        page=PagePath.ABOUT,
        title=LeftNavigationTitle.ABOUT,
        icon=Icon.INFO,
    )

    binary_search: StreamlitPage = streamlit.Page(
        page=PagePath.BINARY_SEARCH,
        title=LeftNavigationTitle.BINARY_SEARCH,
        icon=Icon.SEARCH_CHECK,
    )

    insertion_sort: StreamlitPage = streamlit.Page(
        page=PagePath.INSERTION_SORT,
        title=LeftNavigationTitle.INSERTION_SORT,
        icon=Icon.SORT,
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
