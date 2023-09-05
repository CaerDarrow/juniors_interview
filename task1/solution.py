import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_arguments = sig.bind(*args, **kwargs)

        for name, value in bound_arguments.arguments.items():
            if name in func.__annotations__ and not isinstance(value, func.__annotations__[name]):
                raise TypeError(
                    f"Аргумент '{name}' не соответствует типу '{func.__annotations__[name].__name__}'"
                )

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError