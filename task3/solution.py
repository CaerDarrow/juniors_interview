def appearance(intervals: dict[str, list[int]]) -> int:
    """Получение время общего присутствия ученика и учителя на уроке.

    Алгоритм.
    Создаем дополнительный список интервалов всех событий трех объектов.
    Теперь проходимся по очереди трех объектов и проверяем: новый интервал
    входит ли в том интервале. Рассматриваемый интревал должен быть во всех
    объектах.

    Будем проверять начало интервала. Поэтому важно, чтобы не было нулевых
    интервалов, как и присутствие, так и отсутствие.
    [100, 120, 120, 189] - не будет работать.
    [100, 120, 130, 130, 150, 190] - тоже не будет работать.
    """

    def filter_not_same(items: list[int]) -> list[int]:
        """Получение списка с удалением парных одинаковых элементов."""
        for ki, item in enumerate(items[1:]):
            if items[ki] == item:
                break
        else:
            return items
        res = []
        ki = 1
        while ki < len(items):
            if items[ki-1] == items[ki]:
                ki += 2
                continue
            res.append(items[ki-1])
            ki += 1
        res.append(items[-1])
        return res

    def change_unsuitable_interval(changing_intervals: list[list[int, bool], ],
                                   initial_intervals: list[int]) -> None:
        """Изменение интервала на False, если он не входит в исходном."""
        kc, kj = 0, 0
        while kj < len(initial_intervals):
            while changing_intervals[kc][0] < initial_intervals[kj]:
                changing_intervals[kc][1] = False
                kc += 1
            while changing_intervals[kc][0] < initial_intervals[kj+1]:
                kc += 1
            kj += 2

        while kc < len(changing_intervals):
            changing_intervals[kc][1] = False
            kc += 1

    lesson = filter_not_same(intervals['lesson'])
    pupil = filter_not_same(intervals['pupil'])
    tutor = filter_not_same(intervals['tutor'])

    total_event = set(lesson)
    total_event.update(pupil)
    total_event.update(tutor)
    total_event = sorted([item, True] for item in total_event)

    change_unsuitable_interval(total_event, lesson)
    change_unsuitable_interval(total_event, pupil)
    change_unsuitable_interval(total_event, tutor)

    res = 0
    for ki, item in enumerate(total_event[0:-1]):
        if item[1]:
            res += total_event[ki+1][0] - item[0]
    return res


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                             1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117,
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                             1594704512, 1594704513, 1594704564, 1594705150,
                             1594704581, 1594704582, 1594704734, 1594705009,
                             1594705095, 1594705096, 1594705106, 1594706480,
                             1594705158, 1594705773, 1594705849, 1594706480,
                             1594706500, 1594706875, 1594706502, 1594706503,
                             1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                             1594705149, 1594706463]},
     'answer': 3577,
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565,
     },
]

my = {'intervals': {'lesson': [2000, 5600],
                    'pupil': [2033, 2057, 2057, 2073, 2880, 2880, 5000, 6347],
                    'tutor': [2017, 2066, 2068, 6341]},
      'answer': 638,
      }


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
