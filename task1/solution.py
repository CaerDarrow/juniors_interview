import inspect


def strict(input_func):
    def output(*args):
        type_args_dict = (input_func.__annotations__)
        args_from_input_func = inspect.signature(input_func).bind(*args)
        args_from_input_func.apply_defaults()
        arguments = args_from_input_func.arguments
        for arg, value in arguments.items():
            if not isinstance(value, type_args_dict[arg]):
                raise TypeError
        return input_func(*args)

    return output


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
@strict
def bool_check(a:str,b:bool):
    return f"{a}{b}"


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
