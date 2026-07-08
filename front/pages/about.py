"""About page describing the purpose of the Visualgo application."""

import streamlit as st

st.set_page_config(page_title="About Visualgo")

st.title("WELCOME to Visualgo!")
st.markdown(
    """
    **Visualgo** is my first pet-project app built specifically for
    visualisation and deep understanding famous algorithms implementation.

    **👈 Select an algorithm from the sidebar** to see some examples
    of how it works!

    ### Want to explore more of my pet-projects?
    - Check out [my GitHub repositories](https://github.com/srt-2000?tab=repositories)
    """,
)
