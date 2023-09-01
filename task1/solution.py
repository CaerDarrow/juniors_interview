import functools
import inspect

def strict(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args) -> any:
        val = func(*args)
        types_of_args = inspect.get_annotations(func)
        check_types = all(map(lambda x: x[0] is x[1], (zip(map(type, args + (val,)), types_of_args.values()))))
        if check_types:
            return val
        raise TypeError
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def mul_str(a: int, b: str, c: bool) -> str:
    if c:
        return a * b
    return b

def test_sum_two():
    assert sum_two(5, -3) == 2
    try:
        sum_two(1, 2.4)
        assert False
    except TypeError:
        pass
    try:
        sum_two(1, True)
        assert False
    except TypeError:
        pass

def test_mul_str():
    assert mul_str(5, 'a', True) == 'aaaaa'
    assert mul_str(5, 'a', False) == 'a'
    try:
        mul_str('a', 'a', True)
        assert False
    except TypeError:
        pass

test_sum_two()
test_mul_str()
