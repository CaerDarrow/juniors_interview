import unittest

from main import sum_two

class TestStrictDecorator(unittest.TestCase):
    def test_valid_types(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(0, 0), 0)
        self.assertEqual(sum_two(-5, 5), 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
        with self.assertRaises(TypeError):
            sum_two("warcraft", 'top')
        with self.assertRaises(TypeError):
            sum_two(True, 2)
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
