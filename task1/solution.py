""" Решение первой задачи. """
from typing import Callable
# import unittest


def strict(f: Callable) -> Callable:
    def wrapper(*args) -> Callable:
        # https://docs.python.org/3/library/stdtypes.html#typesmapping
        # "Changed in version 3.7: Dictionary order is guaranteed to be insertion order.
        # This behavior was an implementation detail of CPython from 3.6."
        for i, (arg_name, arg_class) in enumerate(f.__annotations__.items()):
            if arg_name != 'return':
                if not isinstance(args[i], arg_class):
                    raise TypeError("Argument {} is wrong type. Missing a {}, but use a {}.".
                                    format(arg_name, arg_class, args[i].__class__))
        return f(*args)
    return wrapper


@strict
def sum_two(a: int, b: int = 5) -> int:
    return a + b


@strict
def foo(a: str, b: float, c: bool) -> float:
    return True


# class Tests(unittest.TestCase):
#     def tests(self):
#         self.assertRaises(TypeError, sum_two, [2, bool])
#         self.assertRaises(TypeError, foo, [2, bool, 3])

if __name__ == '__main__':
    # unittest.main()
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
