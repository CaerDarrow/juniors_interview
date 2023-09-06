def strict(func):  # декоратор
    def wrapper(*args, **kwargs):
        for i, type in zip(args, func.__annotations__.values()):  # перебираем аргументы и аннотации типов
            if not isinstance(i, type):  # проверяем, соответствует ли тип аргумента ожидаемому типу
                return TypeError("TypeError")  # возвращаем объект TypeError, если типы не совпадают (можно raise еще)
        return func(*args, **kwargs)  # исходная функция
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError