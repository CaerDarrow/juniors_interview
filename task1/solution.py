def strict(func):
    def wrapper(*args, **kwargs):
        arguments = func.__annotations__
        full_arguments = list(args)
        full_arguments.extend(list(kwargs.values()))
        for variable, variable_type in zip(full_arguments, 
                                           list(arguments.values())):
            if not isinstance(variable, variable_type):
                raise TypeError("incorrect type of arguments passed")

        result = func(*args, **kwargs)

        if not isinstance(result, arguments['return']):
            raise TypeError("the result of the function does not match the declared type")

        return result
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_two_incorrect_result(a: int, b: int) -> int:
    return (a + b) / 105.85
