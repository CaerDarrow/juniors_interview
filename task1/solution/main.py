from functools import wraps
from typing import Callable


def check_if_object_type(__object: object, __type: type) -> None:
    """Function for checking object type or raising an exception."""
    if type(__object) is not __type:
        raise TypeError(f"Type {__type} expected, got {__object.__class__}.")


def strict(func: Callable):
    """Strict typing decorator function."""
    @wraps(func)
    def inner(*args, **kwargs):
        annotations: dict = func.__annotations__.copy()
        if 'return' in annotations:
            annotations.pop("return")
        if len(annotations) != len(args) + len(kwargs):
            raise ValueError(f"Expected {len(annotations)} arguments, got {len(args) + len(kwargs)} arguments.")
        keys = list(annotations.keys())
        for idx, arg in enumerate(args):  # check positional arguments
            check_if_object_type(arg, annotations.pop(keys[idx]))

        for key, value in kwargs.items():    # check keyword arguments
            check_if_object_type(value, annotations[key])

        # pass if there wer not exceptions
        return func(*args, **kwargs)

    return inner
