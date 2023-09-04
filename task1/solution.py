import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        types = inspect.get_annotations(func).values()

        for arg, type in zip(args, types):
            if not isinstance(arg, type):
                raise TypeError
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two_int(a: int, b: int) -> int:
    return a + b

@strict
def sum_two_str(a: str, b: str) -> str:
    return a + b


if __name__ == '__main__':
    print(sum_two_int(1, 2))
    print(sum_two_str('1', '2'))
