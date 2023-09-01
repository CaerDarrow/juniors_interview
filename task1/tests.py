import unittest

# Здесь должен быть ваш код с декоратором @strict
from solution import strict


class TestStrictDecorator(unittest.TestCase):

    @strict
    def sum_two(self, a: int, b: int) -> int:
        return a + b

    @strict
    def multiply(self, x: float, y: float) -> float:
        return x * y

    @strict
    def concatenate(self, s1: str, s2: str) -> str:
        return s1 + s2

    @strict
    def bool_operation(self, flag: bool) -> bool:
        return not flag

    def test_int_args(self):
        self.assertEqual(self.sum_two(1, 2), 3)

    def test_float_args(self):
        self.assertEqual(self.multiply(2.5, 3.5), 8.75)

    def test_str_args(self):
        self.assertEqual(self.concatenate("Hello, ", "world!"), "Hello, world!")

    def test_bool_arg(self):
        self.assertEqual(self.bool_operation(True), False)

    def test_mixed_args(self):
        with self.assertRaises(TypeError):
            self.sum_two(1, 2.5)

        with self.assertRaises(TypeError):
            self.concatenate("Hello, ", 42)

    def test_missing_annotation(self):
        @strict
        def func_without_annotation(x):
            return x

        self.assertEqual(func_without_annotation(42), 42)


if __name__ == '__main__':
    unittest.main()
