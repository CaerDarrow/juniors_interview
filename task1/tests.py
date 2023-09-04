import unittest
from solution import sum_two


class TestSumTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_two(4, 5), 9)

    def test_2(self):
        with self.assertRaises(TypeError):
            sum_two(4, True)

    def test_3(self):
        with self.assertRaises(TypeError):
            sum_two(False, 1)

    def test_4(self):
        with self.assertRaises(TypeError):
            sum_two(True, 4.3)

    def test_5(self):
        with self.assertRaises(TypeError):
            sum_two(4, 2.6)

    def test_6(self):
        with self.assertRaises(TypeError):
            sum_two(8, "7")

    def test_7(self):
        with self.assertRaises(TypeError):
            sum_two(4, True)

    def test_8(self):
        self.assertEqual(sum_two(1000, -1000), 0)

    def test_9(self):
        with self.assertRaises(TypeError):
            sum_two("5", 4)


if __name__ == '__main__':
    unittest.main()