def strict(func):
    def wrapper(*args, **kwargs):
        arg_annotations = func.__annotations__

        for i, arg in enumerate(args):
            param_name = list(arg_annotations.keys())[i]
            expected_type = arg_annotations.get(param_name)

            if expected_type is not None and not isinstance(arg, expected_type):
                raise TypeError

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b



print(sum_two(1, 2))
print(sum_two(1, 2.4))
