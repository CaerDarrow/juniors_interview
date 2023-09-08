import asyncio

'''
В первой задаче можно было при вызове ошибки использовать вместо класса TypeError
его экземпляр TypeError('description')

Во второй задаче можно было использовать API википедии!!!
Перед тем как что-то парсить, подумай есть ли у ресурса API.
Всегда пытайся решить задачу проще и не изобретать велосипед.

О Тетрике:
0. Основная деятельность - репетиторские онлайн занятия
1. 4 команды разрабов + 1 тестировщиков (50 чел)
2. Сейчас у них монолит на Tornado с добавлениями модулей на 
FastAPI и aiohttp (планируют растаскивать на модули)
3. Стек: Postgres, Redis
4. Пишут чисты SQL запросы без ORM, крч как я в диалоге
5. В качестве джиры используют Яндекс Трекер
6. В основном удалёнка (Др компании зимой)

Темы которые надо доизучить:
1. Цикл событий
2. Метакласс пораждает класс
3. 23 паттерна проектирования
4. Интерфейс - абстрактный класс только с одними заглушками
5. Фасад - паттерн проектирования смысл, которого в прослойке,
например создание сложного класса загрузки данных в БД, который
будет посредником между клиентами (другими разрабами) и самой БД
7. GIL
8. gather в async

'''


# .............Создание декоратора, который принимает аргументы .............
def any_dec(text):
    def any_dec_in(any_fun):
        def wrapper(*args, **kwargs):
            print(f' start {text}')
            value = any_fun(*args, **kwargs)
            print(f' stop')
            return value

        return wrapper

    return any_dec_in


# Два способа декорирования
additional_arg = "something"


# @any_dec('additional_arg')
def some():
    return print('some')


some = any_dec('additional_arg')(some)

# Вызов функции
some()


# .............Порядок выполнения асинхронного кода .............
async def func1(t):
    print('start 1')
    await asyncio.sleep(t)
    print('stop 1')
    return 1


async def func2(t: int):
    print('start 2')
    await asyncio.sleep(t)
    print('stop 2')


async def main():
    # Функции выполняются по порядку
    # await func1(2)
    # await func2(2)

    # Функции выполняются параллельно
    await asyncio.gather(func1(2), func2(2))


asyncio.run(main())


######### Цикл событий в Python ##########


# .............Классы .............
class B:
    def __iter__(self):
        return self

    def __next__(self):
        return 1


class A:
    def __init__(self, iter_class):
        self.iter_class = iter_class

    def __iter__(self):
        return self.iter_class()  # возвращаем объект класса!


# Обычное итерирование
myclass = B()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

# Возможность передавать классу свойства другого класса итератора
myclass = A(B)
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
