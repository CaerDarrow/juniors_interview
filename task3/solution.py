def trunc_times(times: list[int], st_time: int, end_time: int) -> list[int]:
    """Функция для обрезания временных промежутков по началу и концу урока"""
    min_i = 0
    max_i = len(times) - 1
    for i in range(len(times) - 1):
        if times[i] <= st_time < times[i + 1]:
            if i % 2 == 0:
                min_i = i
                times[min_i] = st_time
            else:
                min_i = i + 1
        if times[i] <= end_time < times[i + 1]:
            if i % 2 == 0:
                max_i = i + 1
                times[max_i] = end_time
            else:
                max_i = i
    return times[min_i:max_i + 1]


def unioun_times(person: list[int]) -> int:
    """Функция для объедения пересекающихся временных промежутков"""
    i, j = 0, 2
    result = []
    while i < len(person):
        while j < len(person) and person[j] <= person[i + 1]:
            person[i + 1] = max(person[j + 1], person[i + 1])
            j += 2
        result.extend((person[i], person[i + 1]))
        i = j
        j += 2
    return result


def intersection_times(pupil: list[int], tutor: list[int]) -> int:
    """Функция для вычесления пересечения времени ученика и учителя"""
    t_i, p_i = 0, 0
    summ = 0
    while t_i < len(tutor):
        while p_i < len(pupil) and pupil[p_i] < tutor[t_i + 1] and pupil[p_i + 1] > tutor[t_i]:
            v1 = pupil[p_i + 1] - pupil[p_i]
            v2 = tutor[t_i + 1] - tutor[t_i]
            v3 = pupil[p_i + 1] - tutor[t_i]
            v4 = tutor[t_i + 1] - pupil[p_i]
            min_time = min(v1, v2, v3, v4)
            summ += min_time
            if v1 == min_time or v3 == min_time:
                p_i += 2
            else:
                break
        t_i += 2
    return summ


def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson, end_lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    pupil = unioun_times(pupil)
    tutor = unioun_times(tutor)
    trunc_times_pupil = trunc_times(pupil, start_lesson, end_lesson)
    trunc_times_tutor = trunc_times(tutor, start_lesson, end_lesson)
    summ = intersection_times(trunc_times_pupil, trunc_times_tutor)
    return summ


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
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
