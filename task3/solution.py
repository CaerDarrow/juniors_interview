def merge_and_remove_included_intervals(intervals: list) -> list:
    """
    Объединяет перекрывающиеся интервалы в списке и удаляет вложенные интервалы.
    :param intervals: Список интервалов, представленных в формате [start1, stop1, start2, stop2, ...]
    :return:Список интервалов после объединения и удаления вложенных интервалов.
    """
    result = []

    for i in range(0, len(intervals), 2):
        start = intervals[i]
        stop = intervals[i + 1]

        merged = False
        for j in range(len(result) // 2):
            existing_start = result[j * 2]
            existing_stop = result[j * 2 + 1]

            if (start <= existing_stop and stop >= existing_start) or (
                    existing_start <= stop and existing_stop >= start):
                start = min(start, existing_start)
                stop = max(stop, existing_stop)
                result[j * 2] = start
                result[j * 2 + 1] = stop
                merged = True
                break

        if not merged:
            result.append(start)
            result.append(stop)

    return result


def clean_intervals(intervals:list, start:int, end:int)->list:
    """
    Делает интервалы соответствующими заданым start и end,если значение интервала start меньше переданного в функцию
    start, то оно заменяется на start, если end интервала больше переданного в функцию end, то оно заменяется на end
    в итоговый результат добавляются только те интервалы,которые входят в интервал переданных в функцию start и end
    :param intervals: Список интервалов, представленных в формате [start1, stop1, start2, stop2, ...]
    :param start: int например 1594702800
    :param end: int например 1594706400
    :return: Список интервалов после обработки
    """
    new_intervals = []
    for i in range(0, len(intervals) - 1, 2):
        start_interval = intervals[i]
        end_interval = intervals[i + 1]
        if start_interval < start:
            start_interval = start
        elif end_interval > end:
            end_interval = end
        if start_interval < end and end_interval > start:
            new_intervals.append(start_interval)
            new_intervals.append(end_interval)
    return new_intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Подсчитывает время общего присутствия ученика и учителя на уроке
    :param intervals: Список интервалов, представленных в формате [start1, stop1, start2, stop2, ...]
    :return: int - количество секунд
    """
    result = 0
    pupil = intervals.get("pupil")
    tutor = intervals.get("tutor")
    start_lesson = intervals.get('lesson')[0]
    end_lesson = intervals.get('lesson')[1]
    new_pupil = merge_and_remove_included_intervals(clean_intervals(pupil, start_lesson, end_lesson))
    new_tutor = merge_and_remove_included_intervals(clean_intervals(tutor, start_lesson, end_lesson))
    for i in range(0, len(new_pupil) - 1, 2):
        star_pupil = new_pupil[i]
        end_pupil = new_pupil[i + 1]
        for j in range(0, len(new_tutor) - 1, 2):
            start_tutor = new_tutor[j]
            end_tutor = new_tutor[j + 1]
            if end_tutor > star_pupil and end_pupil > start_tutor:
                result += min(end_tutor, end_pupil) - max(start_tutor, star_pupil)
    return result


# Тестовые случаи
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
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
