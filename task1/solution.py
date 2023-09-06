from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        types_params = func.__annotations__

        for param, arg in zip(types_params, args):
            if not isinstance(arg, types_params[param]):
                raise TypeError(f"Параметр '{param}' должен иметь тип {types_params[param].__name__}")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
