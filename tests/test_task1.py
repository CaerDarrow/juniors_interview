import pytest
from task1.solution import strict


@strict
def sum_two(a: int, b: int):
    return a + b


@strict
def sum_floats(a: float, b: float):
    return a + b


@strict
def concate_strings(a: str, b: str):
    return a + b


@strict
def is_true(a: bool):
    if a:
        return 'It is true!'
    return 'It is false!'


@strict
def do_stuff(a: bool, b: int, c: float, d: str):
    if not a:
        return d
    return b + c


def test_strict_without_exceptions():
    """Check normal work of `strict` decorator without raising exceptions."""
    assert sum_two(1, 2) == 3
    assert sum_floats(1.5, 2.3) == 3.8
    assert concate_strings('Hello, ', 'Tetrika!') == 'Hello, Tetrika!'
    assert is_true(True) == 'It is true!'
    assert is_true(False) == 'It is false!'
    assert do_stuff(True, 1, 2.5, 'Done!') == 3.5
    assert do_stuff(False, 1, 2.5, 'Done!') == 'Done!'


def test_strict_with_exceptions():
    """Check normal work of `strict` decorator with raising exceptions."""
    with pytest.raises(TypeError) as exc:
        assert sum_two(1, 'Oops')
    assert str(exc.value) == "Arg Oops has invalid type. Must be <class 'int'>"

    with pytest.raises(TypeError) as exc:
        assert sum_floats(1.5, 2)
    assert str(exc.value) == "Arg 2 has invalid type. Must be <class 'float'>"

    with pytest.raises(TypeError) as exc:
        assert concate_strings('Hello, ', 2) == 'Hello, Tetrika!'
    assert str(exc.value) == "Arg 2 has invalid type. Must be <class 'str'>"

    with pytest.raises(TypeError) as exc:
        assert is_true(2)
    assert str(exc.value) == "Arg 2 has invalid type. Must be <class 'bool'>"

    with pytest.raises(TypeError) as exc:
        assert do_stuff(2, 1, 2.5, 'Done!')
    assert str(exc.value) == "Arg 2 has invalid type. Must be <class 'bool'>"
