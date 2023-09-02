def strict(func): 
    def _strict(*args):
        i = 0
        for key in func.__annotations__:
            if len(args) == i:
                break
            if func.__annotations__[key] != type(args[i]):
                return TypeError
            i += 1
        return func(*args)
    return _strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

tests = [
    {'a': 1,
     'b': 2,
     'answer': 3
     },
    {'a': 1,
     'b': 2.4,
     'answer': TypeError
     },
    {'a': '1',
     'b': '2',
     'answer': TypeError
     },
    {'a': 555,
     'b': -666/1,
     'answer': TypeError
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = sum_two(test['a'], test['b'])
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
