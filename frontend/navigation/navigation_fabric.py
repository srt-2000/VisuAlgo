"""Build the Streamlit sidebar page map from page containers."""

from streamlit.navigation.page import StreamlitPage

from frontend.navigation.element_settings import LeftNavigationSubMenuNames
from frontend.navigation.pages_containers import (
    AboutPageContainer,
    SearchAlgorithmsPageContainer,
    SortAlgorithmsPageContainer,
)


def get_pages_container() -> dict[str, list[StreamlitPage]]:
    """Assemble sidebar sections and their pages.

    Returns:
        Mapping from section title to the pages listed under it.
        The About section uses an empty title so it sits at the top.
    """
    about_page: list[StreamlitPage] = AboutPageContainer.get_pages()
    search_algorithms_pages: list[StreamlitPage] = SearchAlgorithmsPageContainer.get_pages()
    sort_algorithms_pages: list[StreamlitPage] = SortAlgorithmsPageContainer.get_pages()

    pages_container: dict[str, list[StreamlitPage]] = {
        LeftNavigationSubMenuNames.EMPTY: about_page,
        LeftNavigationSubMenuNames.SEARCHING: search_algorithms_pages,
        LeftNavigationSubMenuNames.SORTING: sort_algorithms_pages,
    }

    return pages_container
