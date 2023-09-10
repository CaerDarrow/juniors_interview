def strict(func):
    def wrapper(*args):
        for type_arg, value in zip(func.__annotations__.values(), args):
            if type_arg != type(value):
                raise TypeError
        result = func(*args)
        return result
    return wrapper
