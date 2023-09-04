def strict(func):
    """
    Декоратор, проверяющий соответствие приходящих переменных на вход их аннотациям.

    :param func: Функция, к которой применяется декоратор.
    :type func: callable

    :return: Обёртка вокруг функции, выполняющая проверку типов аргументов.
    :rtype: callable

    :raises TypeError: Если переданные аргументы не соответствуют аннотациям.
    """
    def wrapper(*args):
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            expected_type = func.__annotations__.get(arg_name)
            if not isinstance(arg_value, expected_type):
                raise TypeError(f'Аргумент "{arg_name}" не соответствует типу '
                                f'{expected_type.__name__}')
        return func(*args)
    return wrapper
