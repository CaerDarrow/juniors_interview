import unittest

from solution import sum_two


class SumTwoTestCase(unittest.TestCase):
    """Тесты для функции sum_two"""

    def test_int(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_float(self):
        with self.assertRaises(TypeError):
            sum_two(2, 2.4)

    def test_bool(self):
        with self.assertRaises(TypeError):
            sum_two(3, True)

    def test_string(self):
        with self.assertRaises(TypeError):
            sum_two(4, '2')


if __name__ == '__main__':
    unittest.main()
