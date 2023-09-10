from task1.solution import strict
import pytest


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def str_to_uppercase(name: str, to_uppercase: bool) -> str:
    if to_uppercase:
        return name.upper()
    return name


@strict
def return_const() -> int:
    return 1


def test_positional_params():
    assert sum_two(2, 3) == 5
    with pytest.raises(TypeError):
        assert sum_two(2, 3.5)
    with pytest.raises(TypeError):
        assert sum_two(2.5, 3)


def test_named_params():
    assert sum_two(2, b=5) == 7
    assert sum_two(a=2, b=5) == 7
    with pytest.raises(TypeError):
        assert sum_two(2, b=3.5)
    with pytest.raises(TypeError):
        assert sum_two(a="a", b=5)


def test_no_params():
    assert return_const() == 1


def test_other_types():
    assert str_to_uppercase("name", True) == "NAME"
    assert str_to_uppercase("name", False) == "name"
    with pytest.raises(TypeError):
        assert str_to_uppercase("abcd", 5)
