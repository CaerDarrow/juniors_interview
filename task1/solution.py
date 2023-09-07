import functools
import inspect
from typing import Callable


def strict(func: Callable) -> Callable:
    """Проверяет соответствия аргументов функции заявленым в аннотации типам.

    :param func: декорируемая функция
    """
    parameters = inspect.signature(func).parameters

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        def check(argument, argument_type):
            if not isinstance(argument, argument_type):
                raise TypeError

        for i, arg in enumerate(args):
            param_name = list(parameters.keys())[i]
            param_type = parameters[param_name].annotation
            check(arg, param_type)

        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            check(arg, param_type)

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
