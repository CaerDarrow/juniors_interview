import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        types = inspect.get_annotations(func).values()

        # types -> dict_values([class_first_arg, class_second_arg, ..., class_return_value])
        for arg, arg_type in zip(args, types):
            if not isinstance(arg, arg_type):
                raise TypeError('')
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
