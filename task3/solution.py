from collections import namedtuple
from typing import List


TimeInterval = namedtuple('TimeInterval', ['start', 'end'])


def normalize_interval_list(times: List[int]) -> List[TimeInterval]:
    result = []
    start = times[0]
    end = times[1]
    index = 0
    while index < len(times):
        cur_start = times[index]
        cur_end = times[index + 1]
        if cur_start <= end:
            end = max(end, cur_end)
        else:
            item = TimeInterval(start=start, end=end)
            result.append(item)
            start = cur_start
            end = cur_end
        index += 2
    item = TimeInterval(start=start, end=end)
    result.append(item)
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]
    pupil_intervals = normalize_interval_list(intervals['pupil'])
    tutor_intervals = normalize_interval_list(intervals['tutor'])
    pupil_index = 0
    tutor_index = 0
    total_time = 0
    while pupil_index < len(pupil_intervals) and tutor_index < len(tutor_intervals):
        pupil_interval = pupil_intervals[pupil_index]
        tutor_interval = tutor_intervals[tutor_index]
        if pupil_interval.end < tutor_interval.start:
            pupil_index += 1
            continue
        if tutor_interval.end < pupil_interval.start:
            tutor_index += 1
            continue
        start = max(lesson_start, tutor_interval.start, pupil_interval.start)
        end = min(lesson_end, tutor_interval.end, pupil_interval.end)
        duration = end - start
        if duration > 0:
            total_time += duration
        if pupil_interval.end < tutor_interval.end:
            pupil_index += 1
        elif tutor_interval.end < pupil_interval.end:
            tutor_index += 1
        else:
            pupil_index += 1
            tutor_index += 1
    return total_time


if __name__ == '__main__':
    test_data = [
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
    for i, test in enumerate(test_data):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
