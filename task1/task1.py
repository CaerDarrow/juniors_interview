def strict(func):
    def wrapper(*args, **kwargs):
        arg_types = func.__annotations__
        list_arg_types = list(arg_types.values())

        for ind, arg in enumerate(args):
            if not isinstance(arg, list_arg_types[ind]):
                raise TypeError(
                   f"Argument {arg} should be of type "
                   f"{list_arg_types[ind].__name__}"
                   f", not {arg.__class__.__name__}"
                )

        for arg_key, arg_value in kwargs.items():
            if not isinstance(arg_value, arg_types[arg_key]):
                raise TypeError(
                    f"Argument {arg_key} should be of type "
                    f"{arg_types[arg_key].__name__}"
                    f", not {arg_value.__class__.__name__}"
                )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
