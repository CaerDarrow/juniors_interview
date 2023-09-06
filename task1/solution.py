def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for name, value in zip(annotations.keys(), args):
            current_type = annotations[name]
            if not isinstance(value, current_type):
                raise TypeError()
        return func(*args, **kwargs)
    return wrapper
