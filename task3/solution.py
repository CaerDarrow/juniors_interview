def appearance(intervals: dict[str, list[int]]) -> int:
    total_time = 0

    lesson_start, lesson_end = intervals['lesson']
    pupil_interval = find_pure_intervals(intervals['pupil'])
    tutor_interval = intervals['tutor']

    for i in range(0, len(pupil_interval), 2):
        pupil_start = pupil_interval[i]
        pupil_end = pupil_interval[i + 1]

        for j in range(0, len(tutor_interval), 2):
            tutor_start = tutor_interval[j]
            tutor_end = tutor_interval[j + 1]

            common_start = max(pupil_start, tutor_start)
            common_end = min(pupil_end, tutor_end)

            if common_start < common_end:

                if common_start < lesson_start:
                    common_start = lesson_start

                if common_end > lesson_end:
                    common_end = lesson_end

                total_time += common_end - common_start

    return total_time

def find_pure_intervals(intervals: list) -> list:
    pure_intervals = [intervals[0], intervals[1]]

    # start looping from the third element to compare the next session 
    # with the session contained in the pure_intervals list
    for i in range(2, len(intervals), 2):
        pupil_start = intervals[i]
        pupil_end = intervals[i + 1]

        if pupil_start < pure_intervals[-1]:
            pupil_start = pure_intervals[-1]

        if pupil_end < pure_intervals[-1]:
            pupil_end = pupil_start
          
        if pupil_start != pupil_end:
            if pupil_start >= pure_intervals[-1] and pupil_end >= pure_intervals[-1]:
                pure_intervals.append(pupil_start)
                pure_intervals.append(pupil_end)
             
    return pure_intervals

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