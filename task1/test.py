import unittest
from solution import strict


@strict
def sum_two_ints(a: int, b: int) -> int:
    return a + b


@strict
def compare_two_bools(a: bool, b: bool) -> bool:
    return a == b


@strict
def format_string_with_args(a: int, b: float, c: str) -> str:
    return f"a: {a}, b: {b}, c: {c}"


@strict
def float_minus_int(a: float, b: int) -> float:
    return a - b


@strict
def return_int(a: int) -> int:
    return a


class TestStrict(unittest.TestCase):
    # Следующие тесты проверяют корректность возвращаемого значения

    def test_sum_two_ints_correct(self):
        res = sum_two_ints(2, 2)
        self.assertEqual(res, 4)

    def test_compare_two_bools_correct(self):
        res = compare_two_bools(True, False)
        self.assertEqual(res, False)

    def test_format_string_with_args_correct(self):
        res = format_string_with_args(c='abc', a=1, b=2.1)
        self.assertEqual(res, f"a: 1, b: 2.1, c: abc")

    def test_float_minus_int_correct(self):
        res = float_minus_int(1.1, b=2)
        self.assertEqual(res, 1.1 - 2)

    def test_return_int_correct(self):
        res = return_int(100000)
        self.assertEqual(res, 100000)

    # Следующие тесты проверяют на вызов TypeError при некорректных типах фактических аргументов

    def test_sum_two_ints_typeerror(self):
        self.assertRaises(TypeError, sum_two_ints, 1, None)

    def test_compare_two_bools_typeerror(self):
        self.assertRaises(TypeError, compare_two_bools, 0, False)

    def test_format_string_with_args_typeerror(self):
        self.assertRaises(TypeError, format_string_with_args, 'F', 2, c=100)

    def test_float_minus_int_typeerror(self):
        self.assertRaises(TypeError, float_minus_int, (10, 20), 20)

    def test_return_int_typeerror(self):
        self.assertRaises(TypeError, return_int, 10.0)

    # Следующие тесты проверяют на вызов KeyError при неправильных ключах в kwargs

    def test_sum_two_ints_keyerror(self):
        self.assertRaises(KeyError, sum_two_ints, a=2, c=None)

    def test_compare_two_bools_keyerror(self):
        self.assertRaises(KeyError, compare_two_bools, b=False, g=10)

    def test_format_string_with_args_keyerror(self):
        self.assertRaises(KeyError, format_string_with_args, 1, 2.2, d='A')

    def test_float_minus_int_keyerror(self):
        self.assertRaises(KeyError, float_minus_int, a=1.2, f=1)

    def test_return_int_keyerror(self):
        self.assertRaises(KeyError, return_int, c=10.0)


if __name__ == '__main__':
    unittest.main()
