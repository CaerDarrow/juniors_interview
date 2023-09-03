import unittest
from typing import NoReturn

from solution import strict


class TestStrictDecorator(unittest.TestCase):

    def test_correct_types(self):
        @strict
        def add(a: int, b: int) -> int:
            return a + b

        self.assertEqual(add(1, 2), 3)

    def test_incorrect_type(self):
        @strict
        def add(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            add(1, '2')

    def test_correct_different_types(self):
        @strict
        def add(a: int, b: float) -> int:
            return a + b

        self.assertEqual(add(1, 2.2), 3.2)

    def test_incorrect_different_types(self):
        @strict
        def add(a: str, b: float) -> NoReturn:
            return len(a) + b

        with self.assertRaises(TypeError):
            add(1, 2.2)

    def test_correct_bool(self):
        @strict
        def choose(a: bool, b: bool) -> bool:
            return any([a, b])

        self.assertEqual(choose(True, False), True)

    def test_incorrect_bool(self):
        @strict
        def choose(a: bool, b: bool) -> NoReturn:
            return any([a, b])

        with self.assertRaises(TypeError):
            choose(1, 2.2)


if __name__ == '__main__':
    unittest.main()
