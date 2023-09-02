def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов из прототипа функции
        types = func.__annotations__.values()

        # Проверяем типы аргументов переданных в вызов функции
        for arg, typ in zip(args, types):
            if type(arg) is not typ:
                raise TypeError(f"Expected {typ.__name__} but got {type(arg).__name__}")

        # Вызываем исходную функцию
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
