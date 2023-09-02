def strict(func):
    def wrap(*args, **kwargs):
        annotations = func.__annotations__
        
        for arg, expected_type in zip(args, annotations.values()):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument {arg} has wronge type {type(arg)}, "
                    f"but expected {expected_type}"
                )
        
        for kwarg, value in kwargs.items():
            if kwarg in annotations and not isinstance(value, annotations[kwarg]):
                raise TypeError(
                    f"Argument {kwarg} has wronge type {type(kwarg)}, "
                    f"but expected type {annotations[kwarg]}"
                )

        return func(*args, **kwargs)
    return wrap


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError