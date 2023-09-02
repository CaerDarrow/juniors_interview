def appearance(intervals):
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    total_presence_time = 0

    for i in range(0, len(pupil_intervals), 2):
        pupil_entry = max(pupil_intervals[i], lesson_start)
        pupil_exit = min(pupil_intervals[i + 1], lesson_end)
        if pupil_entry < pupil_exit:
            for j in range(0, len(tutor_intervals), 2):
                tutor_entry = max(tutor_intervals[j], pupil_entry)
                tutor_exit = min(tutor_intervals[j + 1], pupil_exit)
                if tutor_entry < tutor_exit:
                    total_presence_time += tutor_exit - tutor_entry

    return total_presence_time


# Тестовые данные
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [2800, 6400],
                   'pupil': [2789, 4500, 2807, 4542, 4512, 4513, 4564,
                             5150, 4581, 4582, 4734, 5009, 5095, 5096,
                             5106, 6480, 5158, 5773, 5849, 6480, 6500,
                             6875, 6502, 6503, 6524, 6524, 6579, 6641],
                   'tutor': [35, 364, 2749, 5148, 5149, 6463]},
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
        print(test_answer, test['answer'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
