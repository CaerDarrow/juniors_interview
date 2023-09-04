import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = inspect.get_annotations(func)
        params = inspect.getcallargs(func, *args, **kwargs)
        for key, value in params.items():
            if not annotations[key] is type(value):
                   raise TypeError(f'{value} not is {annotations[key]}')      
        return_value = func(*args, **kwargs)
        return_annotation = annotations.get('return')
        if not return_annotation is type(return_value):
            raise TypeError
        return return_value
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b