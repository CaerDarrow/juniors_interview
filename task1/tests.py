import pytest

from task1.solution import sum_two, bool_check


def test_sum2():
    assert sum_two(1, 2) == 3


def test_bool_str():
    assert bool_check("1", False) == "1False"


def test_bool_str_error():
    with pytest.raises(TypeError):
        bool_check(1, False)


def test_bool_str_error_2():
    with pytest.raises(TypeError):
        bool_check("1", "False")


def test_sum_error():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)
