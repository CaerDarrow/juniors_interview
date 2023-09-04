import unittest

from solution import appearance, correct_interval


class TestIntervals(unittest.TestCase):

    def test_1(self):
        data = [3340, 3389, 3390, 3395, 3396, 6472]
        return self.assertEqual(correct_interval(data), [3340, 3389, 3390, 3395, 3396, 6472])

    def test_2(self):
        data = [2, 4, 3, 5, 7, 8]
        return self.assertEqual(correct_interval(data), [2, 5, 7, 8])

    def test_3(self):
        data = [
            1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
            1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
            1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
            1594706524, 1594706524, 1594706579, 1594706641
        ]
        correct = [1594702789, 1594704542, 1594704564, 1594706480, 1594706500, 1594706875]
        return self.assertEqual(correct_interval(data), correct)

    def test_4(self):
        data = [1, 3, 4, 5, 2, 4]
        return self.assertEqual(correct_interval(data), [1, 5])

    def test_5(self):
        data = [1, 7, 15, 19, 23, 24, 2, 12]
        return self.assertEqual(correct_interval(data), [1, 12, 15, 19, 23, 24])


class TestAppearance(unittest.TestCase):

    def test_1(self):
        data = {'lesson': [1594663200, 1594666800],
                'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
        return self.assertEqual(appearance(data), 3117)

    def test_2(self):
        data = {'lesson': [1594702800, 1594706400],
                'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                          1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                          1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                          1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}
        return self.assertEqual(appearance(data), 3577)

    def test_3(self):
        data = {'lesson': [1594692000, 1594695600],
                'pupil': [1594692033, 1594696347],
                'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}
        return self.assertEqual(appearance(data), 3565)

    def test_4(self):
        data = {'lesson': [100, 3700],
                'pupil': [80, 99, 101, 1500, 1700, 2100, 1800, 2500],
                'tutor': [90, 500, 900, 2000, 2200, 4000]}
        return self.assertEqual(appearance(data), 1599)

    def test_boundary(self):
        data = {
            'lesson': [0, 3600],
            'pupil': [0, 100, 3500, 3600],
            'tutor': [0, 100, 3500, 3600]
        }
        return self.assertEqual(appearance(data), 200)
