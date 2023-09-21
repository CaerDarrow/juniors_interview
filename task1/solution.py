def strict(func):
    def wrapper(*args, **kwargs):# функция обертка
        args = list(args) + list(kwargs.values())
        arg_annt = (v for v in func.__annotations__.values())# генератор состоящий из типов объявленных в прототипе декорируемой функции
        if all(isinstance(bool, t) if type(obj) is bool else isinstance(obj, t) for obj, t in zip(args, arg_annt)):
            return func(*args)
        else:
            raise TypeError
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b
