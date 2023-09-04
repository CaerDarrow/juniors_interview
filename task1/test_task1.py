import pytest
from task1.solution import strict


@strict
def sum_two_int(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_float(a: float, b: float) -> float:
    return a + b


@strict
def sum_two_mix(a: int, b: float) -> float:
    return a + b


@strict
def bool_reverse(a: bool) -> bool:
    return not a


def test_sum_two_int():
    assert sum_two_int(1, 2) == 3
    with pytest.raises(TypeError):
        sum_two_int(1, 2.5)


def test_sum_two_float():
    assert sum_two_float(1.5, 2.5) == 4.0
    with pytest.raises(TypeError):
        sum_two_float(1, 2)


def test_sum_two_mix():
    assert sum_two_mix(1, 2.5) == 3.5
    with pytest.raises(TypeError):
        sum_two_mix(1, 2)


def test_bool_reverse():
    assert bool_reverse(True) == False
    with pytest.raises(TypeError):
        bool_reverse(5)
