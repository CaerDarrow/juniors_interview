# Необходимо реализовать декоратор @strict.
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов,
# объявленным в прототипе функции. (подсказка: аннотации типов аргументов можно получить из
# атрибута объекта функции func.__annotations__ или с помощью модуля inspect).
# При несоответствии типов бросать исключение TypeError.
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str.
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию.

import inspect


def strict(func):
    parameters_dict = inspect.signature(func).parameters
    parameters_list = list(parameters_dict.values())

    def wrapper(*args, **kwargs):
        for param_index, param_value in enumerate(args):
            param = parameters_list[param_index]
            if param.annotation == inspect.Parameter.empty:
                continue
            if type(param_value) != param.annotation:
                raise TypeError(f'Параметр {param.name} должен иметь тип {param.annotation.__name__}, '
                                f'не {type(param_value).__name__}')
        for param_name, param_value in kwargs.items():
            param = parameters_dict[param_name]
            if param.annotation == inspect.Parameter.empty:
                continue
            if type(param_value) != param.annotation:
                raise TypeError(f'Параметр {param.name} должен иметь тип {param.annotation.__name__}, '
                                f'не {type(param_value).__name__}')
        return func(*args, **kwargs)
    return wrapper






