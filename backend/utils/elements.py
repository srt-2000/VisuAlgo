"""Helpers for Streamlit number widgets."""


def get_int_slider_mid_value(min_value: int, max_value: int) -> int:
    """Pick the integer halfway between two slider ends.

    The binary-search page uses this as the starting target, so the
    input opens in the middle of the chosen range.

    Args:
        min_value: Smallest number on the slider.
        max_value: Largest number on the slider.

    Returns:
        Midpoint, rounded down when the distance is odd.
    """
    mid_value: int = (min_value + max_value) // 2

    return mid_value
