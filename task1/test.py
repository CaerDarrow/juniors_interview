import unittest

from .solution import strict, sum_two_int, sum_two_str


class Testing(unittest.TestCase):

    def test_right_cases(self):
        self.assertEqual(sum_two_int(1, 2), 3)
        self.assertEqual(sum_two_int(10, 20), 30)
        self.assertEqual(sum_two_str('5', '5'), '55')

    def test_wrong_cases(self):
        self.assertRaises(TypeError, sum_two_int, (1, 2.4))
        self.assertRaises(TypeError, sum_two_str, ('1', 2.4))
        self.assertRaises(TypeError, sum_two_str, (1, 0))


if __name__ == '__main__':
    unittest.main()
