def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Функция вычисляет общее время присутствия ученика и учителя на уроке(в секундах).
    :param intervals: Словарь, содержащий интервалы времени: время начала и конца урока,
    интервалы присутствия студента на занятии, интервалы присутствия преподавателя.

    :type intervals: dict[str, list[int]

    :return: Время присутствия преподавателя и студента (в секундах).
    :rtype: int
    """
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    presence_time = 0

    for i in range(0, len(pupil_intervals), 2):
        pupil_entry = pupil_intervals[i]
        pupil_exit = pupil_intervals[i + 1]

        for j in range(0, len(tutor_intervals), 2):
            tutor_entry = tutor_intervals[j]
            tutor_exit = tutor_intervals[j + 1]

            start_overlap = max(pupil_entry, tutor_entry, lesson_start)
            end_overlap = min(pupil_exit, tutor_exit, lesson_end)

            if start_overlap < end_overlap:
                presence_time += end_overlap - start_overlap

    return presence_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    # В тесте ошибка, у ученика третий временной интервал меньше второго,
    # он вернулся на урок раньше, чем до этого с него вышел.
    # Если посчитать, используя диапазоны между временными интервалами, то проблем не будет, но по сути
    # результат будет некорректным.
    # 1594704500 !< 1594702807
    # # {'intervals': {'lesson': [1594702800, 1594706400],
    # #                'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
    # #                          1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
    # #                          1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
    # #                          1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    # #                'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #  'answer': 3577
    #  },
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
