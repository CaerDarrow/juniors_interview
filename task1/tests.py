from contextlib import nullcontext as nc

import pytest
from pytest import raises as rs
from solution import sum_two


@pytest.mark.parametrize(
    "a, b, expected, error",
    [
        (2, 2, 4, nc()),
        (0.8, 'Tuk', True, rs(TypeError))
    ]
)
def test_sum_two(a, b, expected, error):
    with error:
        assert sum_two(a, b) == expected
