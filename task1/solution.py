def strict(func):
    def wrapper(*args, **kwargs):
        result = [True if type(item) == type(args[0]) else False
                  for item in args]
        if not all(result):
            raise TypeError

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
