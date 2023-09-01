def strict(func):
    def wrapper(*args, **kwargs):
        arg_types = func.__annotations__
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in arg_types:
                expected_type = arg_types[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(f"Argument '{arg_name}' should be of type {expected_type.__name__}")
        result = func(*args, **kwargs)
        return_type = arg_types.get('return', None)
        if return_type and not isinstance(result, return_type):
            raise TypeError(f"Return value should be of type {return_type.__name__}")

        return result

    return wrapper
