from functools import wraps
from collections.abc import Callable


def strict(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = list(zip(func.__annotations__.values(), args))

        for expected_type, arg in data:
            if not isinstance(arg, expected_type):
                raise TypeError(f'Expect {expected_type} type, but given {arg} with type {type(arg)}')

        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))

try:
    print(sum_two(1, 2.4))  # >>> TypeError
except TypeError as e:
    print(e)
