from solution import strict,sum_two
from unittest import TestCase, main

class SumFuncTest(TestCase):
    def testStrictErrorRise(self):
        self.assertRaises(TypeError, strict,sum_two(1,'some string'))
    
    def testSum(self):
        self.assertEqual(sum_two(2,4), 6)
    

if __name__=='__main__':
    main()