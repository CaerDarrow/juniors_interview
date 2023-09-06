import unittest
from solution import strict


class TestStrictDecorator(unittest.TestCase):

    def test_sum_two_int(self):
        @strict
        def sum_two_int(i1: int, i2: int) -> int:
            return i1 + i2
        self.assertEqual(sum_two_int(1, 2), 3)
        with self.assertRaises(TypeError):
            sum_two_int(1, 2.4)

    def test_sum_two_str(self):
        @strict
        def sum_two_str(s1: str, s2: str) -> str:
            return s1 + s2
        self.assertEqual(sum_two_str("Test", " strict_decorator"), "Test strict_decorator")
        with self.assertRaises(TypeError):
            sum_two_str("Test", 42)

    def test_sum_two_float(self):
        @strict
        def sum_two_float(f1: float, f2: float) -> float:
            return f1 + f2
        self.assertEqual(sum_two_float(5.0, 2.0), 7.0)
        with self.assertRaises(TypeError):
            sum_two_float(5, "2.0")

    def test_bool_and_bool(self):
        @strict
        def bool_and_bool(b1: bool, b2: bool) -> bool:
            return b1 and b2
        self.assertTrue(bool_and_bool(True, True))
        self.assertFalse(bool_and_bool(True, False))
        with self.assertRaises(TypeError):
            bool_and_bool(True, 42)


if __name__ == "__main__":
    unittest.main()
