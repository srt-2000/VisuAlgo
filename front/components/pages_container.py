"""Container for Streamlit navigation pages used by the application."""

import streamlit
from streamlit.navigation.page import StreamlitPage


class PagesContainer:
    """Holds and exposes Streamlit pages for application navigation.

    Each class attribute of type ``StreamlitPage`` is treated as a registered
    navigation entry.
    """

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

    @classmethod
    def get_pages(cls) -> list[StreamlitPage]:
        """Return all configured ``StreamlitPage`` instances.

        Inspects class attributes and collects every value that is a
        ``StreamlitPage`` instance and is not callable.

        Returns:
            Pages available for Streamlit navigation.
        """
        pages: list[StreamlitPage] = []

        for page in cls.__dict__.values():
            if not callable(page) and isinstance(page, StreamlitPage):
                pages.append(page)
        return pages
