"""Tests for the `ElementPositionFinder` binary search behavior."""

from src.binary_search import ElementPositionFinder


class TestElementPositionFinder:
    """Validate correctness and edge cases of `ElementPositionFinder`."""

    def test_instantiation(self, finder: ElementPositionFinder) -> None:
        """`ElementPositionFinder` can be instantiated via the fixture."""
        assert isinstance(finder, ElementPositionFinder)

    def test_start_index_values(self, finder: ElementPositionFinder) -> None:
        """Initial index boundaries are set to zero."""
        assert finder.max_index == 0
        assert finder.min_index == 0

    def test_binary_search_with_filled_list(
        self,
        filled_list: list[int],
        finder: ElementPositionFinder,
    ) -> None:
        """Binary search returns correct indices for existing elements."""
        assert finder.binary_search(filled_list, 3) == 2
        assert finder.binary_search(filled_list, 9) == 8
        assert finder.binary_search(filled_list, 9) != 9
        assert finder.binary_search(filled_list, 10) is None

    def test_binary_search_with_empty_list(
        self,
        empty_list: list[int],
        finder: ElementPositionFinder,
    ) -> None:
        """Binary search gracefully handles empty input sequences."""
        assert finder.binary_search(empty_list, 0) is None
        assert finder.binary_search(empty_list, 9) is None
