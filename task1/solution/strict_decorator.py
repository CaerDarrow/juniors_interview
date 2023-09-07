from .errors import StrictAnnotationTypeError, StrictUnknownKeywordError


def strict(func):
    """
    Данный декоратор проверяет аннотации типов с фактическими параметрами.
    Проверяемые параметры могут находиться как в args, так и в kwargs.
    Если проверка прошла успешно, то функция выполняется, иначе поднимается ошибка StrictAnnotationTypeError,
    наследующаяся от TypeError.
    Если в kwargs передан неправильный key, то поднимется ошибка StrictUnknownKeywordError,
    наследующаяся от KeyError.
    Примеры:

    @strict
    def sum_two_ints(a: int, b: int) --> int:
        return a + b
    При вызове sum_two_ints(2, 2) функция пройдет валидацию типов и вернет результат.\n
    При вызове sum_two_ints(2,2.2) функция не пройдет валидацию типов и поднимет ошибку StrictAnnotationTypeError.\n
    При вызове sum_two_ints(a=2, c=3) функция поднимет ошибку StrictUnknownKeywordError.\n
    """

    def wrapper(*args, **kwargs):

        # Получаем аннотации типов аргументов
        arg_annotations = func.__annotations__
        # склеиваем зипом имена и значения аргументов без ключей
        # примерный вид zip'а:
        # zip((a, 2), (b, True), (c, <__main__.ClassName object at 0x...>)
        args_with_names = zip(arg_annotations.keys(), args)

        # Проверяем типы значений в args
        for arg_name, arg_value in args_with_names:
            expected_type = arg_annotations[arg_name]

            if not isinstance(arg_value, expected_type):
                raise StrictAnnotationTypeError(func.__name__, arg_name, arg_value.__class__, expected_type)

        # Проверяем типы значений в kwargs
        for arg_name, arg_value in kwargs.items():
            if arg_name not in arg_annotations:
                raise StrictUnknownKeywordError(arg_name, func.__name__)
            expected_type = arg_annotations[arg_name]

            if not isinstance(arg_value, expected_type):
                raise StrictAnnotationTypeError(func.__name__, arg_name, arg_value.__class__, expected_type)

        # Возвращаем первоначальную функцию
        return func(*args, **kwargs)

    return wrapper
