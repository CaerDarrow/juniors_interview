import inspect


def strict(func):
    def wrapper(*args):
        for i in range(len(args)):
            arg_name = inspect.getfullargspec(func).args[i]
            arg_type = func.__annotations__[arg_name]
            if type(args[i]) != arg_type:
                raise TypeError("%s\'s argument %s should be %s type" % (func.__name__, arg_name, arg_type.__name__))
        result = func(*args)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError



