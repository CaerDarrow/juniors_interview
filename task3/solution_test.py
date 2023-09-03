from solution import appearance
import unittest

class SumTwoTestCase(unittest.TestCase):

    def test_appearance(self):
        test_data = {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
            'answer': 3117 
        }
        appearance_func = appearance(test_data['intervals'])
        self.assertEqual(appearance_func, test_data['answer'])



if __name__ == '__main__':
    unittest.main()
