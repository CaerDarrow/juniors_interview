import unittest

from task1.solution import strict


@strict
def val_return(a: int, b: str, c: int) -> tuple:
    return a, b, c


class TaskOneTest(unittest.TestCase):
    def test_1(self):
        res = val_return(1, "1", 1)
        self.assertEqual(res, (1, "1", 1))

    def test_2(self):
        with self.assertRaises(TypeError):
            val_return(1, "1", "1")

    def test_3(self):
        res = val_return(1, c=1, b="1")
        self.assertEqual(res, (1, "1", 1))

    def test_4(self):
        with self.assertRaises(TypeError):
            val_return(1, "1", 4.6)

    def test_5(self):
        with self.assertRaises(TypeError):
            val_return(1, "1")
