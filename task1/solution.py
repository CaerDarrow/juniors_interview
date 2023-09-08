POSSIBLE_TYPES = {str, bool, int, float}


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__.copy()
        return_type = annotations.pop('return')
        for (k, v), a in zip(annotations.items(), args):
            if not v == type(a) or type(a) not in POSSIBLE_TYPES:
                raise TypeError
        func_return_value = func(*args, **kwargs)
        if not return_type == type(func_return_value) or type(func_return_value) not in POSSIBLE_TYPES:
            raise TypeError
        return func_return_value

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))
print(sum_two(1, 2.4))
