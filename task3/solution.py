from data import tests


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    time_total = 0

    while True:  # цикл пробега по всем данным
        for i in range(0, len(pupil_intervals), 2):  # цикл для пробега по ученикам
            pupil_start = pupil_intervals[i]  # вход
            pupil_end = pupil_intervals[i + 1]  # выход

            for j in range(0, len(tutor_intervals), 2):  # цикл для пробега по учителям
                tutor_interval_start = tutor_intervals[j]
                tutor_interval_end = tutor_intervals[j + 1]

                # выбираем самое позднее из этих временных меток, которое будет являться началом пересечения интервалов
                start_overlap = max(pupil_start, tutor_interval_start, lesson_start)
                # выбираем самое раннее из этих временных меток, которое будет являться концом пересечения интервалов
                end_overlap = min(pupil_end, tutor_interval_end, lesson_end)

                # проверка на пересечение интервалов
                if start_overlap <= end_overlap:
                    time_total += end_overlap - start_overlap

        return time_total


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'



