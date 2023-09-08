def calculate_intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    if overlap_start < overlap_end:
        return overlap_end - overlap_start
    return 0


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = [(
        intervals['pupil'][i], intervals['pupil'][i+1]
    ) for i in range(0, len(intervals['pupil']), 2)
    ]
    tutor_intervals = [(
        intervals['tutor'][i], intervals['tutor'][i+1]
    ) for i in range(0, len(intervals['tutor']), 2)
    ]
    total_presence = 0
    for pupil_interval in pupil_intervals:
        for tutor_interval in tutor_intervals:
            total_presence += calculate_intersection(
                pupil_interval, tutor_interval
            )
    return total_presence


def test_appearance():
    tests = [
        {'intervals': {
            'lesson': [1594663200, 1594666800],
            'pupil': [
                1594663340, 1594663389, 1594663390,
                1594663395, 1594663396, 1594666472
            ],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
            'answer': 3117},
        {'intervals': {
            'lesson': [1594702800, 1594706400],
            'pupil': [
                1594702789, 1594704500, 1594702807,
                1594704542, 1594704512, 1594704513,
                1594704564, 1594705150, 1594704581,
                1594704582, 1594704734, 1594705009,
                1594705095, 1594705096, 1594705106,
                1594706480, 1594705158, 1594705773,
                1594705849, 1594706480, 1594706500,
                1594706875, 1594706502, 1594706503,
                1594706524, 1594706524, 1594706579, 1594706641
            ],
            'tutor': [
                1594700035, 1594700364, 1594702749,
                1594705148, 1594705149, 1594706463
            ]},
            'answer': 3577},
        {'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
            'answer': 3565},
    ]
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == (
            test['answer'],
            f'Error on test case {i}, got {test_answer}, '
            f'expected {test["answer"]}'
        )
    print("All tests passed!")


if __name__ == '__main__':
    test_appearance()
