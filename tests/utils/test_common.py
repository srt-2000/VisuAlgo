"""Unit tests for ``unpack_sublists_to_array``."""

import pytest

from backend.utils.common import unpack_sublists_to_array
from tests.utils.cases import INVARIANTS_UNPACK_SUBLISTS


class TestUnpackSublistsToArray:
    """Check that nested int lists flatten in the original order."""

    @pytest.mark.parametrize("invariant", INVARIANTS_UNPACK_SUBLISTS)
    def test_invariants(self, invariant: tuple[list[int], ...]) -> None:
        """Keep length and element order after flattening."""
        unpacked_result: tuple[int, ...] = unpack_sublists_to_array(invariant)
        unpacked_result_len: int = len(unpacked_result)
        index_base: int = 0
        expected_result_len: int = sum([len(sublist) for sublist in invariant])

        assert unpacked_result_len == expected_result_len
        assert isinstance(unpacked_result, tuple)

        for i in range(len(invariant)):
            sub_list: list[int] = invariant[i]
            sub_len: int = len(sub_list)

            for j in range(sub_len):
                current_unpacked_index: int = index_base + j
                unpacked_element: int = unpacked_result[current_unpacked_index]
                invariant_element: int = invariant[i][j]

                assert unpacked_element == invariant_element

            index_base += sub_len
