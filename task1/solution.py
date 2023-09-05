def strict(func):
    def wrapper(*args):
        declared_types = func.__annotations__.values()
        given_types = [type(arg) for arg in args]
        for declared_type, given_type in zip(declared_types, given_types):
            if not declared_type == given_type:
                raise TypeError('Variable types do not match decorated')
        return func(*args)

    return wrapper
