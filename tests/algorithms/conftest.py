"""Pytest fixtures shared by algorithm unit tests."""

import pytest


@pytest.fixture(scope="function")
def sorted_filled_list_with_nine_elements() -> list[int]:
    """Provide a small sorted list ``[1, 2, ..., 9]``.

    Returns:
        Non-empty sorted list of ints.
    """
    return list(range(1, 10))
