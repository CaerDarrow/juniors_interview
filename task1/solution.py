

def strict(func):
    def inner(*args, **kwargs):
        for arg, type in zip(args, func.__annotations__.values()):
            if not isinstance(arg, type):
                raise TypeError
        return func(*args, **kwargs)
    return inner

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError