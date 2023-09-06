'''
python3.9 ubuntu
Необходимо реализовать декоратор @strict
Декоратор проверяет соответствие типов переданных
в вызов функции аргументов типам аргументов, объявленным
в прототипе функции. (подсказка: аннотации типов
можно получить из атрибута объекта функции func.__annotations__
или с помощью модуля inspect) При несоответствии типов бросать
исключение TypeError Гарантируется, что параметры в декорируемых
функциях будут следующих типов: bool, int, float, str Гарантируется,
что в декорируемых функциях не будет значений параметров, заданных
по умолчанию
'''


def strict(func):
    def chek_type(x, y):
        if type(x) == func.__annotations__['a']:
            if type(y) == func.__annotations__['b']:
                outcome = func(x, y)
            else:
                print('"Ошибка. Измените тип аргумента"')
                raise TypeError
        return outcome
    return chek_type


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
