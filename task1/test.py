from .solution import strict
import pytest


@strict
def f1(a: int, b: int) -> int:
    return a + b


@strict
def f2(a, b: bool, c: str):
    pass


@pytest.mark.parametrize('args', [[1, 2],
                                 [3, 4],])
def test_f1_with_correct_args(args):
    f1(*args)


@pytest.mark.parametrize('args', [[1, True, 'abc'],
                                   [1.1, False, 'def'],
                                   [None, True, '']])
def test_f2_with_correct_args(args):
    f2(*args)


@pytest.mark.parametrize('args', [[0, 0.1],
                                  [0.0, 1],
                                 [None, False],
                                 ['1', '2'],])
def test_f1_with_other_type_args(args):
    with pytest.raises(TypeError) as e_info:
        f1(*args)


@pytest.mark.parametrize('args', [[None, 0, '1'],
                                   [0, True, None],
                                   [False, 1, ['a', 'b']]])
def test_f2_with_other_type_args(args):
    with pytest.raises(TypeError) as e_info:
        f2(*args)
