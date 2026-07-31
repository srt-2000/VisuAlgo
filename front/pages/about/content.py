"""Markdown body text for the About page."""

from enum import StrEnum


class PageContent(StrEnum):
    """Long text blocks shown on the About page."""

    WELCOME_CONTENT = """
    **Visualgo** is my first pet-project app built specifically for
    visualisation and deep understanding famous algorithms implementation.

    **👈 Select an algorithm from the sidebar** to see some examples
    of how it works!

    ### Want to explore more of my pet-projects?
    - Check out [my GitHub repositories](https://github.com/srt-2000?tab=repositories)
    """
