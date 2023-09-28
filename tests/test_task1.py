import pytest
from task1.solution import sum_two


def test_sum_two_with_int():
    res = sum_two(1, 2)
    assert res == 3


def test_sum_two_with_float():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)


def test_sum_two_with_negative_numbers():
    result = sum_two(-3, 5)
    assert result == 2


def test_sum_two_with_zero():
    result = sum_two(0, 0)
    assert result == 0
