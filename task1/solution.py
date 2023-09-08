def strict(func):
    def wrapper(*args, **kwargs):
        first_type = type(args[0])
        for i in args:
            if type(i) != first_type:
                raise TypeError()
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a, b) -> int:
    return a + b

print(sum_two(1, 2.1))
