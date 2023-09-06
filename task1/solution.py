from functools import wraps
import inspect

def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        
        for name, value in bound_args.arguments.items():
            if name in annotations and not isinstance(value, annotations[name]):
                raise TypeError(f"Argument '{name}' should be of type '{annotations[name].__name__}'")
        
        return func(*args, **kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

