# =============
# from . import some




def any_dec(text):
    def any_dec_in(any_fun):
        def wrapper(*args, **kwargs):
            print(f' start {text}')
            value = any_fun(*args, **kwargs)
            print(f' stop')
            return value

        return wrapper

    return any_dec_in


...

# @any_dec('fsdgssg')
any_dec = any_dec('fsdgssg')(some)


def some():
    return print('some')


some()
some = any_dec('gsg')(some)


# text = 'dsfafa'
# some = any_dec(some)
# some(text)


# s = any_dec(text='dsfafa')
# @s
# def some2():
#   return print('some')


# class A():
#   ...


async def func1():
    print('start 1')
    await asyncio.sleep(1)
    print('stop 1')
    return 1


async def func2(a: int):
    print('start 2')
    await asyncio.sleep(a)
    print('stop 2')

async main():
while True:
    await ...

res = func1()
await func2(res)


class B:
    def __next__(self):
        return 1


class A:
    def __init__(iter_class)
        self.iter_class = iter_class

    def __iter__(self):
        return self.iter_class