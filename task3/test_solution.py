from solution import appearance, tests
from unittest import TestCase, main

intervals = {'lesson': [1, 6],
             'pupil': [3, 4], #1
             'tutor': [2, 4]  #2
}

class TestAppearance(TestCase):
    def testAppearanceEqual(self):
        self.assertEqual(appearance(intervals), 1)
    def testNoneArgument(self):
        self.assertIsNone(tests)



if __name__=='__main__':
    main()