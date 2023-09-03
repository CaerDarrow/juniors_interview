import unittest

from solution import appearance, _generate_timestamp_set


class TestSolution(unittest.TestCase):

    def test_from_real_data(self):
        intervals = {
            'lesson': [60, 180],
            'pupil': [50, 55, 65, 75, 80, 120, 125, 175],
            'tutor': [40, 45, 70, 170],
        }

        self.assertEqual(appearance(intervals), 90)

    def test_out_of_lesson(self):
        intervals = {
            'lesson': [60, 180],
            'pupil': [50, 55, 185, 200],
            'tutor': [40, 45, 185, 210],
        }

        self.assertEqual(appearance(intervals), 0)

    def test_full_overlap(self):
        intervals = {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692000, 1594695600],
            'tutor': [1594692000, 1594695600]
        }

        self.assertEqual(appearance(intervals), 3600)

    def test_empty_intervals(self):
        intervals = {
            'lesson': [1594692000, 1594695600],
            'pupil': [],
            'tutor': []
        }

        self.assertEqual(appearance(intervals), 0)

    def test_generate_timestamp_set_funk(self):
        intervals = [1594663200, 1594666800]

        result = _generate_timestamp_set(intervals)
        expected_result = set(range(1594663200, 1594666800))

        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()
