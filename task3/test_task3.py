from solution import appearance
import unittest


class TestWorkTime(unittest.TestCase):
    # Тест с обоими присутствующими - учеником и учителем
    def test_both_present(self):
        intervals = {'lesson': [100, 200], 'pupil': [110, 130, 150, 180], 'tutor': [105, 125, 160, 190]}
        self.assertEqual(appearance(intervals), 45)

    # Тест, когда ни ученик, ни учитель не присутствуют
    def test_neither_present(self):
        intervals = {'lesson': [300, 400], 'pupil': [], 'tutor': []}
        self.assertEqual(appearance(intervals), 0)

    # Тест, когда интервалы ученика и учителя совпадают с интервалом урока
    def test_intervals_equal_lesson(self):
        intervals = {'lesson': [200, 300], 'pupil': [100, 200, 300, 400], 'tutor': [150, 250, 280, 320]}
        self.assertEqual(appearance(intervals), 0)


if __name__ == '__main__':
    unittest.main()
