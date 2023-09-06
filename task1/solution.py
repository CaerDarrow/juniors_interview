from typing import Any


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = tuple(func.__annotations__.items())
        args_annotations = zip(args, annotations)
        for arg_value, (annotate_key, annotate_type) in args_annotations:
            if annotate_type == Any:
                raise TypeError(f"Для точности аннотаций нельзя передавать {Any}")
            if annotate_type != type(arg_value):
                raise TypeError(
                    f"Аргумент {annotate_key} должен быть типа: {annotate_type}.\n"
                    f"Вы передали {arg_value} - типа {type(arg_value)}"
                )
        result = func(*args, **kwargs)
        if type(result) != annotations[-1][1]:
            raise TypeError(
                f"Результат функции должен быть типа: {annotations[-1][1]}. "
                f"У вас получился результат {result} типа {type(result)}"
            )
        return result

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
