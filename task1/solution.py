

def strict(func):
    def inner(*args):
        z = list(zip(args, func.__annotations__.values()))
        if not all(type(x[0]) == x[1] for x in z):
            raise TypeError(
                f'Несовпадение типов данных: {z}'
            )
        return func(*args)
    return inner


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
