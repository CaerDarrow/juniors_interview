def transform_intervals(interval, start_lesson, end_lesson):
    for i in range(1, len(interval), 2):
        interval[i] = min(end_lesson, interval[i])
        interval[i-1] = max(start_lesson, interval[i-1])
    return interval


def appearance(intervals: dict[str, list[int]]) -> int:
    pupil = transform_intervals(
        intervals['pupil'],
        intervals['lesson'][0],
        intervals['lesson'][1]
    )
    tutor = transform_intervals(
        intervals['tutor'],
        intervals['lesson'][0],
        intervals['lesson'][1]
    )

    tmp_start = tutor[0]
    total = 0
    for i in range(1, len(tutor), 2):
        for j in range(1, len(pupil), 2):
            if tmp_start < pupil[j]:
                start = max(tutor[i-1], pupil[j-1])
                end = min(tutor[i], pupil[j])
                if start > end:
                    continue
                if start > tmp_start:
                    tmp_start = start
                total += end - tmp_start
                tmp_start = end
    return total


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
