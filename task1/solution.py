def strict(func):
    """Декоратор проверяет соответствие типов, переданных в вызов
    функции аргументов типам аргументов, объявленным в прототипе функции.
    """
    def wrapper(*args, **kwargs):
        """Внутренняя функция декоратора"""

        VALID_TYPES = {
            int: (int,),
            float: (int, float),
            bool: (bool,),
            str: (str,),
        }

        def check_type(value, type_):
            """Проверка типа."""
            if type(value) not in VALID_TYPES.keys():
                raise TypeError(
                    'Допустимы только '
                    f'{tuple(item.__name__ for item in VALID_TYPES.keys())}'
                )
            if type(value) not in VALID_TYPES[type_]:
                raise TypeError(f'Задано {value} ({type(value).__name__}), '
                                f'но должно быть {type_}')

        from collections import OrderedDict
        annotations = OrderedDict(func.__annotations__)
        return_func = (annotations.pop('return') if 'return' in annotations
                       else None)
        if len(args) + len(kwargs) != len(annotations):
            raise TypeError('Неправильное количество аргументов.')
        for key, value in kwargs.items():
            if key not in annotations:
                raise TypeError(f'Неизвестная переменная {key}')
            check_type(value, annotations[key])
            annotations.pop(key)
        for value, key in zip(args, annotations):
            check_type(value, annotations[key])
        return_value = func(*args, **kwargs)
        return return_value
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def multy_three(c: int, b: float, a: float) -> float:
    return c*b*a


if __name__ == '__main__':
    # print(sum_two(1, 2))  # >>> 3
    assert sum_two(1, 2) == 3

    # print(sum_two(1, 2.4))  # >>> TypeError

    # print(multy_three(3.5, '5', a=45.))
    # print(multy_three(3, '5', a=45.))
    # print(multy_three(3, 5, a=45.))
    # print(multy_three(3, a=False, b=45.))
