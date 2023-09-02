def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        print(annotations)

        # Check positional arguments
        for arg, expected_type in zip(args, annotations.values()):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument {arg} is not of expected type {expected_type}"
                )

        # Check keyword arguments
        for kwarg, value in kwargs.items():
            if kwarg in annotations and not isinstance(value, annotations[kwarg]):
                raise TypeError(
                    f"Argument {kwarg} is not of expected type {annotations[kwarg]}"
                )

        return func(*args, **kwargs)

    return wrapper


# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
