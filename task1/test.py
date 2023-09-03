from solution import strict


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

if __name__ == '__main__':
    test_sum_two()
    test_mul_str()
