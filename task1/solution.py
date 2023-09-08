import functools
import unittest


def strict(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        param_types = func.__annotations__
        for i, arg in enumerate(args):
            arg_name = list(param_types.keys())[i]
            expected_type = param_types[arg_name]
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}'"
                    f"должен иметь тип {expected_type.__name__}"
                )
        for arg_name, arg_value in kwargs.items():
            expected_type = param_types.get(arg_name)
            if expected_type is None:
                raise TypeError(f"Неверный агрумент '{arg_name}'")
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}'"
                    f"должен иметь тип {expected_type.__name__}"
                )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


class TestStrictDecorator(unittest.TestCase):
    def test_valid_arguments(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(0, 0), 0)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
        with self.assertRaises(TypeError):
            sum_two("hello", 2)

    def test_unexpected_keyword_argument(self):
        with self.assertRaises(TypeError):
            sum_two(a=1, b=2)

        with self.assertRaises(TypeError):
            sum_two(1, 2, c=3)


if __name__ == '__main__':
    unittest.main()
