def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        annotation_keys = list(annotations.keys())
        for num, name in enumerate(args):
            if 'args' in annotation_keys:
                instance = annotations[annotation_keys[num]] if num < annotation_keys.index('args')\
                    else annotations.get('args')
            else:
                instance = annotations[annotation_keys[num]]
            if type(name) != instance:
                raise TypeError(f'{name} type is not correct')
        for key, value in kwargs.items():
            instance = annotations.get(key) if key in annotations else annotations.get('kwargs')
            if type(value) != instance:
                raise TypeError(f'{key} type is not correct')

        return func(*args, **kwargs)

    return wrapper


@strict
def sum(a: int, b: int) -> int:
    """
    Sum of two numbers, a and b
    """
    return a + b


@strict
def names(sender: int, *args: str) -> str:
    """
    Greeting to people from args
    """
    return f'- {sender}: Hello {", ".join(args)}!'


@strict
def check_true(**kwargs: bool) -> list:
    """
    List of true parameters
    """
    truth = list()
    for key, value in kwargs.items():
        truth.append(key) if value else None
    return truth


@strict
def float_sum(a: float, b: float) -> float:
    """
    Sum of two float numbers
    """
    return a + b


@strict
def everything(first: bool, second: str, *args: int, **kwargs: float):
    return None
