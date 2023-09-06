import unittest

from task1.solution import strict

"""
Файл придется запускать командой python -m unittest task1.test_solution в терминале
"""


class TestStrictDecorator(unittest.TestCase):
    @strict
    def add_two_integers(self, a: int, b: int) -> int:
        return a + b

    @strict
    def multiply_two_floats(self, a: float, b: float) -> float:
        return a * b

    def test_correct_integers(self):
        result = self.add_two_integers(2, 3)
        self.assertEqual(result, 5) 

    def test_incorrect_integers(self):
        with self.assertRaises(TypeError):
            self.add_two_integers(2, 3.5)  

    def test_correct_floats(self):
        result = self.multiply_two_floats(2.5, 3.0)
        self.assertEqual(result, 7.5)  

    def test_incorrect_floats(self):
        with self.assertRaises(TypeError):
            self.multiply_two_floats(2.5, 3)  
