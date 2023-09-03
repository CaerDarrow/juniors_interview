def make_clear_intervals(intervals: list[int]) -> list[int]:
    '''Объединяет пересекащиеся интервалы.'''
    result = [*intervals[:2]]
    for i, start_interval in enumerate(intervals):
        if i == 0 or i % 2 != 0:
            continue
        end_interval = intervals[i + 1]
        if result[-1] >= start_interval:
            result[-1] = max(end_interval, result[-1])
        else:
            result.extend(intervals[i:i + 2])
    return result


def make_intersecting_intervals(
        intervals1: list[int], intervals2: list[int]) -> list[int]:
    '''Создает список пересекающихся значений входящих списков.'''
    intersecting_intervals = []
    i, j = 0, 0
    while i <= len(intervals1) - 1 and j <= len(intervals2) - 1:
        checking_interval1 = intervals1[i:i+2]
        checking_interval2 = intervals2[j:j+2]
        if checking_interval2[1] <= checking_interval1[0]:
            j += 2
            continue
        if checking_interval2[0] >= checking_interval1[1]:
            i += 2
            continue
        intersecting_intervals.append(max(
            checking_interval1[0], checking_interval2[0])
                                      )
        intersecting_intervals.append(
            min(checking_interval1[1], checking_interval2[1])
            )
        if intersecting_intervals[-1] == checking_interval1[1]:
            i += 2
        if intersecting_intervals[-1] == checking_interval2[1]:
            j += 2
    return intersecting_intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    '''Получает на вход словарь с интервалами и возвращает время общего
    присутствия ученика и учителя на уроке (в секундах).'''
    intersecting_intervals = make_intersecting_intervals(
        make_clear_intervals(intervals['pupil']),
        make_clear_intervals(intervals['tutor'])
        )
    intersecting_intervals = make_intersecting_intervals(
        intersecting_intervals, intervals['lesson']
        )
    result = 0
    for i, start_interval in enumerate(intersecting_intervals):
        if i % 2 != 0:
            continue
        end_interval = intersecting_intervals[i + 1]
        result += end_interval - start_interval
    return result
