import pytest
from task3.solution import appearance, fix_intervals


@pytest.mark.parametrize('intervals, answer', [
    ({'lesson': [1594663200, 1594666800],
      'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
      'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     3117),
    ({'lesson': [1594702800, 1594706400],
      'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
      'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     3577),
    ({'lesson': [1594692000, 1594695600],
      'pupil': [1594692033, 1594696347],
      'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     3565),
])
def test_appearance(intervals, answer):
    assert appearance(intervals) == answer


@pytest.mark.parametrize('pupil_or_tutor, start_lesson, end_lesson, expected_result', [
    ([1, 2, 3, 4, 5], 3, 6, [3, 3, 3, 4, 5]),
    ([6, 7, 8, 9, 10], 3, 6, [6, 6, 6, 6, 6]),
    ([1, 2, 3, 4, 5], 1, 5, [1, 2, 3, 4, 5]),
])
def test_fix_intervals(pupil_or_tutor, start_lesson, end_lesson, expected_result):
    fix_intervals(pupil_or_tutor, start_lesson, end_lesson)
    assert pupil_or_tutor == expected_result
