import unittest

from solution import strict


@strict
def add_ints(a: int, b: int) -> int:
    return a + b


@strict
def add_floats(a: float, b: float) -> float:
    return a + b


@strict
def concatenate_strings(a: str, b: str) -> str:
    return ' '.join([a, b])


@strict
def check_bool(a: bool):
    if a:
        return '42'


class TestDecorator(unittest.TestCase):

    def test_integers_valid(self):
        res = add_ints(2, 3)
        self.assertEqual(res, 5)

    def test_integers_invalid(self):
        with self.assertRaises(TypeError):
            add_ints(2, 3.5)

    def test_floats_valid(self):
        res = add_floats(2.5, 3.5)
        self.assertEqual(res, 6)

    def test_floats_invalid(self):
        with self.assertRaises(TypeError):
            add_floats(2.5, False)

    def test_concatenation(self):
        res = concatenate_strings('Hello', 'World!')
        self.assertEqual(res, 'Hello World!')

    def test_concatenation_invalid(self):
        with self.assertRaises(TypeError):
            concatenate_strings('Hello', 5)

    def test_bool(self):
        res = check_bool(True)
        self.assertEqual(res, '42')

    def test_bool_invalid(self):
        with self.assertRaises(TypeError):
            check_bool(5)


if __name__ == '__main__':
    unittest.main()
