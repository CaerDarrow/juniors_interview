from typing import Any
from functools import wraps
import inspect

def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        print(annotations)
        b_args = inspect.signature(func).bind(*args, **kwargs)
        for name, value in b_args.arguments.items():
            if type(value) == bool:
                raise TypeError(
                        f'Argumen "{name}" shoud be of type "{annotations[name].__name__}" '
                        f"Your argument '{value}' - type of {type(value)}"
                    )
            if name in annotations and not isinstance(value, annotations[name]):
                raise TypeError(
                        f'Argumen "{name}" shoud be of type "{annotations[name].__name__}"'
                        f"Your argument '{value}' - type of {type(value)}"
                    )
        
        return func(*args, **kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b
