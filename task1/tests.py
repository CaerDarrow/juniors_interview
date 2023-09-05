import pytest
from solution import strict


def test_bool_to_int_args():
    @strict
    def func(first: int, second: int, third: int):
        pass

    with pytest.raises(TypeError) as exc:
        func(False, True, False)
    assert str(exc.value) == 'Variable types do not match decorated'


def test_str_to_bool_args():
    @strict
    def func(first: bool, second: bool):
        pass

    with pytest.raises(TypeError) as exc:
        func('test_string', True)
    assert str(exc.value) == 'Variable types do not match decorated'


def test_random_args():
    @strict
    def func(a: str, b: bool, c: int, d: float):
        return True

    result = False
    test_args = ['a', True, 1, 1.01]
    try:
        result = func(*test_args)
    except TypeError:
        pass
    assert result
