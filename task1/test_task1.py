import unittest

from solution import sum_two


class SumTwoTestCase(unittest.TestCase):
    """Тесты для функции sum_two"""

    def test_int(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
            sum_two(1, True)
            sum_two(1, '2')


if __name__ == '__main__':
    unittest.main()
