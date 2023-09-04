def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов
        annotations = func.__annotations__

        # Проверяем позиционнеы аргументы
        for arg, (param_name, param_type) in zip(args, annotations.items()):
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type {param_type}, but got {type(arg)}.")

        # Проверяем именовынные аргументы
        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name in annotations and not isinstance(kwarg_value, annotations[kwarg_name]):
                raise TypeError(f"Argument '{kwarg_name}' must be of type {annotations[kwarg_name]}, but got {type(kwarg_value)}.")

        return func(*args, **kwargs)

    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
