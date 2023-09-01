"""
Необходимо реализовать декоратор `@strict`
Декоратор проверяет соответствие типов переданных в вызов функции аргументов
типам аргументов, объявленным в прототипе функции.
(подсказка: аннотации типов аргументов можно получить из атрибута объекта
функции `func.__annotations__` или с помощью модуля `inspect`)
При несоответствии типов бросать исключение `TypeError`
Гарантируется, что параметры в декорируемых функциях будут следующих типов:
`bool`, `int`, `float`, `str`
Гарантируется, что в декорируемых функциях не будет значений параметров,
заданных по умолчанию
"""


def strict(func):
    def wrapper(*args):
        fa = list(func.__annotations__.items())
        for i, val in enumerate(args):
            if not isinstance(val, fa[i][1]):
                return TypeError
        result = func(*args)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_float(a: float, b: float) -> float:
    return a + b


@strict
def sum_str(a: str, b: str) -> str:
    return a + b


@strict
def sum_bool(a: bool, b: bool) -> bool:
    return a + b


def test_int():
    assert (sum_two(1, 2)) == 3
    assert (sum_two(1, 2.4)) == TypeError


def test_float():
    assert (sum_float(1.3, 4.2)) == 5.5
    assert (sum_float(1, 2)) == TypeError


def test_str():
    assert (sum_str('asd', 'dasd')) == 'asddasd'
    assert (sum_str(1, 'dwdw')) == TypeError


def test_bool():
    assert (sum_bool(True, True)) == 2
    assert (sum_bool(False, 'eeqwe')) == TypeError
