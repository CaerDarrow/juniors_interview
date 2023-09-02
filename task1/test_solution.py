import unittest
from solution import strict


class TestDecorator(unittest.TestCase):
    def test_sum(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)
        self.assertRaises(TypeError, sum_two, 1, 2.4)
        self.assertRaises(TypeError, sum_two, 'hello', 2)
        self.assertRaises(TypeError, sum_two, True, 2)


if __name__ == "__main__":
    unittest.main()