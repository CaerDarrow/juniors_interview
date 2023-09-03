def strict(func):
    def wrapper(*args):
        if list(func.__annotations__.values())[:-1] == [type(value) for value in args]:
            return func(*args)
        else:
            raise TypeError("Invalid argument type")
    return wrapper


@strict
def sum_two(a: int, b: float) -> int:
    return a + b

try:
    print(sum_two(1, 2))  # >>> 3
except TypeError as exc:
    print(exc)  

try:
    print(sum_two(1, 2.4))
except TypeError as exc:
    print(exc)
