def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        # Проверяем типы позиционных аргументов
        for i, arg in enumerate(args):
            expected_type = annotations[list(annotations.keys())[i]]
            if not isinstance(arg, expected_type):
                raise TypeError(f"Аргумент {arg} должен быть типа {expected_type.__name__}")

        # Проверяем типы именованных аргументов
        for arg_name, arg_value in kwargs.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(f"Аргумент {arg_name} должен быть типа {expected_type.__name__}")

        # Проверяем возвращаемый тип функции
        result = func(*args, **kwargs)
        if not isinstance(result, annotations['return']):
            raise TypeError("Функция вернула неверный тип данных")
        else:
            return result

    return wrapper
