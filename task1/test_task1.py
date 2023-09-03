import unittest
from .solution import sum_two


class TestTask1(unittest.TestCase):
    def test_right_numbers(self):
        self.assertEqual(sum_two(1,2), 3)

    def test_wrong_numbers(self):
        self.assertRaises(TypeError, sum_two, (1, 2.4))


if __name__ == '__main__':
    unittest.main()