def strict(func):
    def wrapper(*args, **kwargs):
        annotations = [val for key, val in func.__annotations__.items() if key != 'return']
        arguments = [type(val) for val in [*args]]
        key_args = {**kwargs}

        for key, val in func.__annotations__.items():
            if key in key_args.keys():
                arguments.append(type(key_args.get(key)))

        if annotations != arguments:
            raise TypeError
        return func(*args, **kwargs)
    return wrapper


# @strict
# def sum_two(a: int, b: str, c: int):
#     return a, b, c

#
# if __name__ == "__main__":
#     print(sum_two(67, c=5.8, b="45"))
