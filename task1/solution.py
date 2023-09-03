#!/usr/bin/env python

def strict(func):
    def wrap(*args, **kwargs):
        annotations = func.__annotations__
        for arg, arg_type in zip(args, annotations.values()):
            if not isinstance(arg, arg_type):
                raise TypeError(f'TypeError: Wrong argument type \"{arg}\". Expected: {arg_type}, received: {type(arg)}')
        return func(*args, **kwargs)
    return wrap

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_three(a: int, b: float, c: bool) -> float:
    return a + b + c

def test():
    assert sum_two(1, 2) == 3
    assert sum_three(1, 2.4, True) == 4.4
    assert sum_three(1, 0.1, False) == 1.1

    try:
        sum_two(1, 2.4)
    except TypeError:
        assert True

    try:
        sum_three(2.4, True, 1)
    except TypeError:
        assert True


test()