import pytest
from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


def test_correct_types():
    assert sum_two(1, 2) == 3


def test_incorrect_types():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)
