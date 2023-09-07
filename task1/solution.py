def strict(func):
    """
    Декоратор проверяет соответствие типов переданных в вызов функции
    аргументов типам аргументов, объявленным в прототипе функции.
    >>> sum_two(1, 2)
    3
    >>> sum_two(1, 2.4)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument b must be <class 'int'>
    >>> sum_two(1.2, 2)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument a must be <class 'int'>
    >>> sum_two(1, '2')
    Traceback (most recent call last):
        ...
    TypeError: Type of argument b must be <class 'int'>
    >>> sum_two('1', 2)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument a must be <class 'int'>
    >>> sum_two(1, True)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument b must be <class 'int'>
    >>> sum_two(False, 2)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument a must be <class 'int'>
    >>> to_str(3, 0.1415926535, ' == number pi is ', True)
    '3.1415926535 == number pi is True'
    >>> to_str('3', 0.1415926535, ' == number pi is ', True)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument a must be <class 'int'>
    >>> to_str(3, 1, ' == number pi is ', True)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument b must be <class 'float'>
    >>> to_str(3, 0.1415926535, False, True)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument c must be <class 'str'>
    >>> to_str(3, 0.1415926535, ' == number pi is ', 0)
    Traceback (most recent call last):
        ...
    TypeError: Type of argument d must be <class 'bool'>
    >>> to_str(3, 0.1415926535, c=' == number pi is ', d=True)
    '3.1415926535 == number pi is True'
    >>> to_str(3, 0.1415926535, d=True, c=' == number pi is ')
    '3.1415926535 == number pi is True'
    >>> to_str(3, 0.1415926535, c=True, d=' == number pi is ')
    Traceback (most recent call last):
        ...
    TypeError: Type of argument c must be <class 'str'>
    >>> to_str(3, 0.1415926535, d=1, c=' == number pi is ')
    Traceback (most recent call last):
        ...
    TypeError: Type of argument d must be <class 'bool'>
    """
    def wrapper(*args, **kwargs):
        message = 'Type of argument {} must be {}'
        annotations = func.__annotations__
        for key, val in zip(annotations, args):
            if annotations[key] != type(val):
                raise TypeError(
                    message.format(key, annotations[key])
                )
        for key, val in kwargs.items():
            if annotations[key] != type(kwargs[key]):
                raise TypeError(
                    message.format(key, annotations[key])
                )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def to_str(a: int, b: float, c: str, d: bool) -> str:
    return str(a + b) + str(c) + str(d)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
