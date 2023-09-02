import unittest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

class TestCase(unittest.TestCase):

    def test_valid_arguments_first(self):
        result = sum_two(1, 2)
        self.assertEqual(result, 3) 

    def test_valid_arguments_second(self):
        result = sum_two(13, 7)
        self.assertEqual(result, 20) 

    def test_valid_arguments_third(self):
        result = sum_two(14, 27)
        self.assertEqual(result, 41) 

    def test_invalid_arguments_first(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.5)

    def test_invalid_arguments_second(self):
        with self.assertRaises(TypeError):
            sum_two(5.1, 2.5)

    def test_invalid_arguments_third(self):
        with self.assertRaises(TypeError):
            sum_two(1.7, 2)


if __name__ == '__main__':
    unittest.main()
