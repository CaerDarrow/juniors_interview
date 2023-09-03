def strict(func):
    def wrapper(*args, **kwargs):
        types = list(func.__annotations__.values())
        for i in range(len(args)):
            if not isinstance(args[i], types[i]):
                raise TypeError
        return func(*args, *kwargs)
    return wrapper

import unittest

class TestStrictDecorator(unittest.TestCase):
    def test_sum_two(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_sub_three(self):
        @strict
        def sub_three(a: float, b: float, c: float) -> float:
            return a - b - c

        self.assertEqual(sub_three(4.5, 1.5, 1.0), 2.0)
        with self.assertRaises(TypeError):
            sub_three(1, 2.4, 5)

if __name__ == '__main__':
    unittest.main()