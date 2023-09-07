def strict(func):
    print(func.__annotations__)
    if func.__annotations__.get('return') == func.__annotations__.get('a') and func.__annotations__.get('b')== func.__annotations__.get('return'):
        return func
    else:
        raise TypeError


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError