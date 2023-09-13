def strict(func):
    def wrapper(*args):# функция обертка
        arg_annt = (v for v in func.__annotations__.values())# генератор состоящий из типов объявленных в прототипе декорируемой функции
        if all(isinstance(bool, t) if type(obj) is bool else isinstance(obj, t) for obj, t in zip(args, arg_annt)):
            return func(*args)
        else:
            raise TypeError
    return wrapper
