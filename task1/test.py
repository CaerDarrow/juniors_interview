import pytest
from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_float(a: float, b: float) -> float:
    return a + b


def test_sum_two_valid_types():
    """Проверка правильности типов."""
    assert sum_two(1, 2) == 3


@pytest.mark.parametrize('values', [(1, 2.4), (True, 2), (3, '4')])
def test_sum_two_invalid_types(values):
    """Ошибка TypeError при неправильные данные"""
    with pytest.raises(TypeError):
        sum_two(values)


@pytest.mark.parametrize('val_1, val_2, result',
                         [(1.6, 2.4, 4), (1, 2, 3),
                          (3.2, 4, 7.2), (1, 1.1, 2.1)
                          ])
def test_sum_float_valid_with_int(val_1, val_2, result):
    """Где флоаты, там можно ставить инт."""
    assert sum_float(val_1, val_2) == result


def test_sum_float_invalid_with_bool():
    """Где флоаты или инты, нельзя ставить bool."""
    with pytest.raises(TypeError):
        assert sum_float(1.1, bool)
        assert sum_two(bool, 4)


@strict
def func2(l: list, d: dict) -> None:
    return l, d


def test_func_invalid_another_type():
    """Поддержутся основные типы int, float, bool, str."""
    with pytest.raises(TypeError):
        assert func2([1, 2, 3], {3: 5, 6: 8})


@strict
def func(a: int, b: bool, c: str, d: float):
    return a, b, c, d


def test_func_wich_keys_valid():
    """Можно использовать ключевые переменные."""
    assert func(3, True, d=1.1, c='test') == (3, True, 'test', 1.1)
    assert func(3, c='test', d=4, b=False) == (3, False, 'test', 4)
