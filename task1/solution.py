def strict(func):
    def wrap(*args):
        classes = [type(arg) for arg in args]
        if classes == list(func.__annotations__.values()):
            return func(*args)
        else:
            raise TypeError
    return wrap
