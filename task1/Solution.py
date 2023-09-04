import pytest

def strict(func):
    def func_accepting_arguments(*args, **kwargs):
        dict_with_args = func.__annotations__
        if kwargs:
            for key,value in kwargs.items():
                if type(value) != dict_with_args[key]:
                    raise TypeError(f'Тип переданного в функцию значения аргумента {key} ({type(value)}) не '
                                    f'соответствует заявленному в аннотации ({dict_with_args[key]})')
        else:
            list_with_args = list(dict_with_args.values())[0:-1]
            for i, value in enumerate(list_with_args):
                if type(args[i]) != value:
                    raise TypeError(f'Тип переданного в функцию значения аргумента номер {i+1} ({args[i]}) '
                                    f'не соответствует заявленному в аннотации ({value})')
        return func(*args, **kwargs)
    return func_accepting_arguments

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_three_words(first: str, second: str, third: str) -> str:
    return f'{first} {second} {third}'


def tests():
    with pytest.raises(TypeError):
        assert sum_two(True, 3) == TypeError
        assert sum_two(2, 'value') == TypeError
        assert sum_two(c=3, z=6) == 9
        assert sum_two(7, b=2) == 9
        assert sum_two(8.0, False) == TypeError
        assert sum_three_words('I', 'am', 'Vadim') == 'I am Vadim'
        assert sum_three_words(second='am', third='Vadim', first='I') == 'I am Vadim'
        assert sum_three_words('f', 'b', 9) == TypeError
        assert sum_three_words(word='word', num=10, float=10.0)

if __name__ == "__main__":
    tests()

