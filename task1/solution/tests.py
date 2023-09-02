import unittest

from main import strict


class TestPositionalArguments(unittest.TestCase):

    @staticmethod
    @strict
    def sum_(a: int, b: int):
        return a + b

    def test_success_ints(self):
        self.assertEqual(self.sum_(12, 2), 14)

    def test_fail_float1_got(self):
        with self.assertRaises(TypeError):
            self.sum_(12.1, 2)

    def test_fail_float2_got(self):
        with self.assertRaises(TypeError):
            self.sum_(12.1, False)

    def test_fail_args_many(self):
        with self.assertRaises(ValueError):
            self.sum_(12.1, 12, 3)


class TestReturnAnnotation(unittest.TestCase):

    @staticmethod
    @strict
    def sum_(a: int, b: int):
        return a + b

    def test_success_ints(self):
        self.assertEqual(self.sum_(12, 2), 14)

    def test_fail_float1_got(self):
        with self.assertRaises(TypeError):
            self.sum_(12.1, 2)

    def test_fail_float2_got(self):
        with self.assertRaises(TypeError):
            self.sum_(12.1, False)

    def test_fail_args_many(self):
        with self.assertRaises(ValueError):
            self.sum_(12.1, 12, 3)


class TestKeywordArguments(unittest.TestCase):

    @staticmethod
    @strict
    def boolean_cast(a: int, b: bool):
        return a and b

    def test_success_ints(self):
        self.assertEqual(self.boolean_cast(1020, False), False)

    def test_fail_float1_got(self):
        with self.assertRaises(TypeError):
            self.boolean_cast(12.1, True)

    def test_fail_float2_got(self):
        with self.assertRaises(TypeError):
            self.boolean_cast(12.1, 13.12)

    def test_fail_args_many(self):
        with self.assertRaises(ValueError):
            self.boolean_cast(12.1, 12, 3)


if __name__ == '__main__':
    unittest.main()
