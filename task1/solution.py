from functools import wraps


def strict(some_func):
    @wraps(some_func)
    def wrap(*args, **kwargs):
        if len(args) + len(kwargs) != len(some_func.__annotations__):
            raise AssertionError('Не у всех параметров указан тип.')

        for arg, type_fn in zip(args, some_func.__annotations__.values()):
            if not isinstance(arg, type_fn):
                raise TypeError(f"Значение '{arg}' не является типом {type_fn}")

        for kw_key, kw_val in kwargs.items():
            if not isinstance(kw_val, some_func.__annotations__[kw_key]):
                raise TypeError(
                    f"Значение '{kw_val}' не является типом "
                    f"{some_func.__annotations__[kw_key]}")

        return some_func(*args, **kwargs)

    return wrap


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
