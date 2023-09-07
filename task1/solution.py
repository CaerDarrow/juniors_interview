import inspect
import typing


def is_type(instance, type_info):
    if type_info == typing.Any:
        return True
    if hasattr(type_info, '__origin__'):
        if type_info.__origin__ in {typing.Union, typing.Optional}:
            return any(is_type(instance, arg) for arg in type_info.__args__)
    return type(instance) is type_info


def strict(func):
    types_info = typing.get_type_hints(func)
    signature = inspect.signature(func)

    def wrapper(*args, **kwargs):
        sig = signature.bind(*args, **kwargs)
        sig.apply_defaults()
        for name, value in sig.arguments.items():
            if not is_type(value, types_info.get(name, typing.Any)):
                raise TypeError(f'{name} is not of the correct type')
        return func(*args, **kwargs)

    return wrapper
