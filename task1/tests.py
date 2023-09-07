import unittest

from solution import sum_two


class TestCase(unittest.TestCase):
    def test_valid_argument_types(self):
        self.assertEqual(sum_two(3, 1), 4)
        self.assertEqual(sum_two(2, 1), 3)

    def test_invalid_argument_types(self):
        self.assertRaises(TypeError, sum_two, ('22', 22))
        self.assertRaises(TypeError, sum_two, (2.0, 2))


if __name__ == '__main__':
    unittest.main()
