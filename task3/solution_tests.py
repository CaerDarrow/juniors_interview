import unittest

from solution import appearance
# from solution2 import appearance


class TestAppearance(unittest.TestCase):

    def test_same_intervals(self):
        intervals = {'lesson': [100, 200], 'pupil': [110, 130, 140, 160], 'tutor': [110, 130, 140, 160]}
        self.assertEqual(appearance(intervals), 40)

    def test_no_student_teacher(self):
        intervals = {'lesson': [100, 200], 'pupil': [], 'tutor': []}
        self.assertEqual(appearance(intervals), 0)

    def test_lesson_within_intervals(self):
        intervals = {'lesson': [1000, 2000], 'pupil': [100, 150, 160, 200], 'tutor': [100, 150, 160, 200]}
        self.assertEqual(appearance(intervals), 0)

    def test_no_intersection(self):
        intervals = {'lesson': [100, 200], 'pupil': [50, 80], 'tutor': [90, 100]}
        self.assertEqual(appearance(intervals), 0)


if __name__ == '__main__':
    unittest.main()
