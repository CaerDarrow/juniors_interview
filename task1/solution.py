import inspect

def strict(func):
    def wrapper(*args):
        arg_names = inspect.getfullargspec(func).args
        for arg, name in zip(args, arg_names):
            if not type(arg) == inspect.get_annotations(func)[name]:
                raise TypeError('Parameter type doesn''t match prototype')
        return func(*args)
    return wrapper
