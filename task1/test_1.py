import unittest

from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


class TestSumTwo(unittest.TestCase):
    def test_two_int(self):
        self.assertEqual(sum_two(2, 3), 5)

    def test_int_float(self):
        self.assertRaises(TypeError, sum_two, (3, 2.4))

    def test_int_boolean(self):
        with self.assertRaises(TypeError):
            sum_two(4, True)

    def test_int_str(self):
        with self.assertRaises(TypeError):
            sum_two(1, "test")

    def test_float_boolean(self):
        with self.assertRaises(TypeError):
            sum_two(1.5, True)

    def test_float_str(self):
        with self.assertRaises(TypeError):
            sum_two(2.3, "test")

    def test_boolean_str(self):
        with self.assertRaises(TypeError):
            sum_two(True, "7")


if __name__ == '__main__':
    unittest.main()
