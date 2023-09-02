def strict(func):
    def wrapper(a, b):
        if func.__annotations__['a'] == type(a) and func.__annotations__['b'] == type(b):
            return func(a, b)
        else:
            raise TypeError

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
