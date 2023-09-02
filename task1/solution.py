import inspect

def strict(func):
    arg_types = func.__annotations__

    def wrapper(*args, **kwargs):
        parameters = inspect.signature(func).parameters

        for arg_name, arg_value in zip(parameters, args):
            if arg_name in arg_types and not isinstance(arg_value, arg_types[arg_name]):
                raise TypeError(f'Argument "{arg_name}" must be of type {arg_types[arg_name]}, but got {type(arg_value)}')

        result = func(*args, **kwargs)

        return_type = arg_types.get('return', None)
        if return_type is not None and not isinstance(result, return_type):
            raise TypeError(f'Return value must be of type {return_type}, but got {type(result)}')

        return result

    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b