def appearance(intervals: dict[str, list[int]]) -> int:
    # Функция возвращает пересечение двух интервалов
    def intersect(interval_a, interval_b):
        # Check if the end of the first interval is before the start of the second interval
        if interval_a[1] < interval_b[0] or interval_b[1] < interval_a[0]:
            return 0, 0
        else:
            return max(interval_a[0], interval_b[0]), min(interval_a[1], interval_b[1])

    # Проверяем правильность интервала(начало интервала раньше, чем конец)
    def is_valid(interval):
        return interval[0] < interval[1]

    # Объединяем пересекающиеся интервалы
    def merge_intervals(intervals_list):
        if not intervals_list:
            return []

        intervals_list.sort(key=lambda x: x[0])
        merged = [intervals_list[0]]

        for current in intervals_list:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:
                merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
            else:
                merged.append(current)

        return merged

    # Записываем время начала и конца урока
    lesson_start, lesson_end = intervals['lesson']

    # Оставляем только интервалы, которые входят в урок
    pupil_intervals = [(max(lesson_start, intervals['pupil'][i]), min(lesson_end, intervals['pupil'][i + 1]))
                       for i in range(0, len(intervals['pupil']), 2) if is_valid(
            intersect((lesson_start, lesson_end), (intervals['pupil'][i], intervals['pupil'][i + 1])))]

    tutor_intervals = [(max(lesson_start, intervals['tutor'][i]), min(lesson_end, intervals['tutor'][i + 1]))
                       for i in range(0, len(intervals['tutor']), 2) if is_valid(
            intersect((lesson_start, lesson_end), (intervals['tutor'][i], intervals['tutor'][i + 1])))]

    # Объединяем интервалы в каждом массиве
    merged_pupil_intervals = merge_intervals(pupil_intervals)
    merged_tutor_intervals = merge_intervals(tutor_intervals)

    intersected_intervals = []

    # Считаем время общего нахождения ученика и учителя на уроке
    for interval_a in merged_pupil_intervals:
        for interval_b in merged_tutor_intervals:
            intersected_intervals.append(intersect(interval_a, interval_b))

    result_duration = sum([interval[1] - interval[0] for interval in intersected_intervals])

    # Возвращаем результат
    return result_duration




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
