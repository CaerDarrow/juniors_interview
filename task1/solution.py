def strict(func):
    def wrapper(*args, **kwargs):
        param_types = func.__annotations__
        for arg_name, arg_value in zip(param_types.keys(), args):
            expected_type = param_types[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}' должен быть типа {expected_type.__name__},"
                    f" но передан {type(arg_value).__name__}")

        result = func(*args, **kwargs)

        return result

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
