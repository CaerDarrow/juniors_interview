def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals, tutor_intervals = intervals['pupil'], intervals['tutor']

    total_presence = 0

    # Получаем точки входа и выхода для ученика
    pupil_enter = pupil_intervals[::2]
    pupil_exit = pupil_intervals[1::2]

    # Получаем точки входа и выхода для учителя
    tutor_enter = tutor_intervals[::2]
    tutor_exit = tutor_intervals[1::2]

    for pupil_ent, pupil_ext in zip(pupil_enter, pupil_exit):
        # Проверяем, что присутствие ученика внутри интервала урока
        if pupil_ent <= lesson_end and pupil_ext >= lesson_start:
            for tutor_ent, tutor_ext in zip(tutor_enter, tutor_exit):
                # Проверяем, что присутствие учителя пересекается с присутствием ученика
                if tutor_ent <= pupil_ext and tutor_ext >= pupil_ent:
                    presence_start = max(pupil_ent, tutor_ent, lesson_start)
                    presence_end = min(pupil_ext, tutor_ext, lesson_end)
                    total_presence += presence_end - presence_start

    return total_presence


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 6757
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
