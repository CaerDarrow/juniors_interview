def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        arg_names = list(annotations.keys())
        # для позиционных аргументов
        for i, arg in enumerate(args):
            arg_name = arg_names[i]
            expected_type = annotations[arg_name]
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}' должен быть типа '{expected_type.__name__}', а получен '{type(arg).__name__}'")
        # для именованных
        for arg_name, arg_value in kwargs.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(
                        f"Аргумент '{arg_name}' должен быть типа '{expected_type.__name__}', а получен '{type(arg_value).__name__}'")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
