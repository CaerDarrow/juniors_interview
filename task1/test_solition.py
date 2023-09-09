import unittest

from solution import sum_two, sum_two_incorrect_result


class TestSolution(unittest.TestCase):
    def test_with_int(self):
        self.assertEqual(sum_two(2,5), 7)

    def test_with_bool(self):
        self.assertRaises(TypeError, sum_two, (False, 4))

    def test_with_float(self):
        self.assertRaises(TypeError, sum_two, (5, 5.5))

    def test_with_str(self):
        self.assertRaises(TypeError, sum_two, (5, "5"))

    def test_with_two_arguments_incorrect(self):
        self.assertRaises(TypeError, sum_two, ("str", 4.5))

    def test_with_incorrect_result_func(self):
        self.assertRaises(TypeError, sum_two_incorrect_result, (3, 5))

    def test_with_kwargs_b(self):
        self.assertEqual(sum_two(5, b = 3), 8)

    def test_with_kwargs_a_b(self):
        self.assertEqual(sum_two(a = 5, b = 3), 8)

    def test_with_incorrect_kwargs_b(self):
        self.assertRaises(TypeError, sum_two, 3, b = 5.5)

    def test_with_incorrect_kwargs_a_b(self):
        self.assertRaises(TypeError, sum_two, a = 3.3, b = 5.5)


if __name__ == '__main__':
    unittest.main()
