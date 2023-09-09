from solution import sum_two
import unittest

class SumTwoTest(unittest.TestCase):
    
    def test_sumtwo(self):
        self.assertEqual(sum_two(2, 1), 3)

    def test_sumtwo_type_error(self):
        with self.assertRaises(TypeError):
            sum_two(2, 2.4)
        
if __name__ == '__main__':
    unittest.main()