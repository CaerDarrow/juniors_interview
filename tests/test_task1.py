from contextlib import nullcontext as does_not_raise

import pytest

from task1.solution import sum_two


@pytest.mark.parametrize(
    "x, y, result, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (3, 3, 6, does_not_raise()),
        (3, "3", 6, pytest.raises(TypeError)),
        ("3", 3, 6, pytest.raises(TypeError)),
        (True, 5, 10, pytest.raises(TypeError)),
        (5, False, 10, pytest.raises(TypeError)),
        ([2], [2], 4, pytest.raises(TypeError)),
    ],
)
def test_sum_two(x, y, result, expectation):
    with expectation:
        assert sum_two(x, y) == result
