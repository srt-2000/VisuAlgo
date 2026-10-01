

def get_int_slider_mid_value(min_value: int, max_value: int) -> int:
    """Getting the middle value for a slider rendering
    Args:
        min_value: Minimum value for the slider
        max_value: Maximum value for the slider
    Returns: int middle value
    """
    mid_value: int = (min_value + max_value) // 2

    return mid_value
