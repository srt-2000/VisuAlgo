"""Holds Streamlit pages used in the app sidebar navigation."""

import streamlit
from streamlit.navigation.page import StreamlitPage

from frontend.element_settings import Icon
from frontend.navigation.element_settings import LeftNavigationTitle, pages_paths


class BasePagesContainer:
    """Collect ``StreamlitPage`` class attributes into a list.

    Subclasses declare pages as class attributes. ``get_pages``
    walks those attributes and returns only the page objects.
    """

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


class AboutPageContainer(BasePagesContainer):
    """Sidebar entry for the About page."""

    about: StreamlitPage = streamlit.Page(
        page=pages_paths.ABOUT,
        title=LeftNavigationTitle.ABOUT,
        icon=Icon.INFO,
    )


class SearchAlgorithmsPageContainer(BasePagesContainer):
    """Sidebar entries for search algorithm pages."""

    binary_search: StreamlitPage = streamlit.Page(
        page=pages_paths.BINARY_SEARCH,
        title=LeftNavigationTitle.BINARY_SEARCH,
        icon=Icon.SEARCH_CHECK,
    )


class SortAlgorithmsPageContainer(BasePagesContainer):
    """Sidebar entries for sorting algorithm pages."""

    insertion_sort: StreamlitPage = streamlit.Page(
        page=pages_paths.INSERTION_SORT,
        title=LeftNavigationTitle.INSERTION_SORT,
        icon=Icon.SORT,
    )

    bubble_sort: StreamlitPage = streamlit.Page(
        page=pages_paths.BUBBLE_SORT,
        title=LeftNavigationTitle.BUBBLE_SORT,
        icon=Icon.SORT,
    )

    selection_sort: StreamlitPage = streamlit.Page(
        page=pages_paths.SELECTION_SORT,
        title=LeftNavigationTitle.SELECTION_SORT,
        icon=Icon.SORT,
    )
