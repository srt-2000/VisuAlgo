import pytest

from tests.algorithms.insertion_sort.cases import NOT_SORTED_ARRAYS


@pytest.fixture(scope="function", params=NOT_SORTED_ARRAYS)
def array(request) -> tuple[list[int],...]:
    """Provide not sorted arrays.

    Returns:
        tuple[list[int]]
    """

    return request.param
