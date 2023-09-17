from unittest import TestCase

from task1.solution import sum_two


class TestSumTwo(TestCase):

    def test_valid(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(True, True), 2)
        self.assertAlmostEqual(sum_two(1.2, 2.4), 3.6, places=1)
        self.assertEqual(sum_two("Jun", "ior"), "Junior")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum_two(1, 1.3)


if __name__ == '__main__':
    unittest.main()
