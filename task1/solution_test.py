from solution import sum_two
import unittest

class SumTwoTestCase(unittest.TestCase):

    def test_sum_two(self):
        sum_two_func = sum_two(3, 4)
        self.assertEqual(sum_two_func, 7)



if __name__ == '__main__':
    unittest.main()
