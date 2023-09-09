import inspect


def strict(func):
    signature = inspect.signature(func) # получаем сигнатуры
    parameter_types = signature.parameters # сохраняем типы ожидвемых аргументов

    def wrapper(*args, **kwargs):
        bound_arguments = signature.bind(*args, **kwargs) # объеденяем ожидаемые типы с переданными аргуменами

        for name, value in bound_arguments.arguments.items():
            expected_type = parameter_types[name].annotation # достаём тип ожидаемого аргумента

            if not isinstance(value, expected_type): # сравниваем полученные аргументы с ожидаемыми типами
                raise TypeError(f"Argument '{name}' must be of type '{expected_type.__name__}'")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

