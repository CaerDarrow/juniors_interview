import functools
import inspect


def strict(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args) -> any:
        val = func(*args)
        types_of_args = inspect.get_annotations(func)
        check_types = all(map(lambda x: x[0] is x[1], zip(map(type, args + (val,)), types_of_args.values())))
        if check_types:
            return val
        raise TypeError
    return wrapper
