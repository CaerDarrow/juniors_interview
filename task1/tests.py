import unittest

from solution import check_true, everything, float_sum, names, sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        return self.assertEqual(sum(1, 2), 3)

    def test_sum_exception(self):
        return self.assertRaises(TypeError, sum, 1, 2.4)


class TestNames(unittest.TestCase):

    def test_names_sender(self):
        out = '- 1: Hello John, Sarah, Bill!'
        return self.assertEqual(names(1, 'John', 'Sarah', 'Bill'), out)

    def test_names_sender_exception(self):
        return self.assertRaises(TypeError, names, 'Me', 'John', 'Bill', 'Sarah')

    def test_names_args_exception(self):
        return self.assertRaises(TypeError, names, 1, 'John', True)


class TestCheckTrue(unittest.TestCase):

    def test_check_true_kwargs(self):
        return self.assertEqual(check_true(a=True, b=True, c=True, e=False), ['a', 'b', 'c'])

    def test_check_true_kwargs_exception(self):
        return self.assertRaises(TypeError, check_true, a=True, b=1)


class TestEverything(unittest.TestCase):

    def test_everything(self):
        return self.assertEqual(everything(True, 'second', 1, 2, 3, 4, 5, a=6.0, b=7.0), None)


class TestFloatSum(unittest.TestCase):

    def test_float_sum(self):
        return self.assertEqual(float_sum(1.0, 2.0), 3.0)
