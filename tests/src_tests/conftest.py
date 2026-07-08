"""Shared pytest fixtures for binary search tests."""

import pytest

from src.binary_search import ElementPositionFinder


@pytest.fixture(scope="class")
def finder() -> ElementPositionFinder:
    """Provide a reusable `ElementPositionFinder` instance for a test class."""
    return ElementPositionFinder()


@pytest.fixture
def filled_list() -> list[int]:
    """Provide a non-empty sorted list of integers for search scenarios."""
    return list(range(1, 10))


@pytest.fixture
def empty_list() -> list[int]:
    """Provide an empty list for edge-case search scenarios."""
    return []
