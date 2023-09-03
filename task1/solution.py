from functools import wraps


def strict(func):
    """
    Decorator which validates passed argument types on declared argument types.
    """

    @wraps(func)
    def inner(*args):
        declared_args_types_list = list(func.__annotations__.values())

        for i in range(len(args)):
            arg = args[i]
            declared_arg_type = declared_args_types_list[i]
            if not isinstance(arg, declared_arg_type):
                raise TypeError(
                    f'Arg {arg} has invalid type. Must be {declared_arg_type}'
                )

        return func(*args)

    return inner
