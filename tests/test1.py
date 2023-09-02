import pytest

from task1.solution.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_str(*args: str):
    return " ".join([s for s in args])


def test_correct_nums():
    assert sum_two(2, 2) == 4


def test_incorrect_nums():
    with pytest.raises(TypeError):
        sum_two(1.1, 2)


def test_correct_str():
    assert sum_str("Hello,", "world") == "Hello, world"


def test_incorrect_str():
    with pytest.raises(TypeError):
        sum_str(1, "abc")
