from typing import Iterable
from numbers import Number


def give_pairs(data: list):
    """Function that converts lists to pairs."""
    for last_idx in range(1, len(data), 2):
        yield data[last_idx - 1: last_idx + 1]


def crop_intervals(min_limit: Number, max_limit: Number, data: list | tuple):
    """Function that crops interval data with given endpoint limits."""
    if data[0] < min_limit:
        data[0] = min_limit
    if data[1] > max_limit:
        data[1] = max_limit
    return data


def prepare_coped_data(lesson: list | tuple, data_source: Iterable):
    """Generator for cropping data list."""
    for data in data_source:
        yield crop_intervals(lesson[0], lesson[1], data)


def appearance(intervals: dict[str, list[int]]) -> int:
    appearance_time = 0
    lesson = intervals['lesson']
    lesson_begin, lesson_finish = intervals['lesson']
    intervals_pupil = list(prepare_coped_data(lesson, give_pairs(intervals['pupil'])))
    intervals_tutor = list(prepare_coped_data(lesson, give_pairs(intervals['tutor'])))
    begin_with_pupil = begin_with_tutor = 0

    while begin_with_pupil < len(intervals_pupil) and begin_with_tutor < len(intervals_tutor):
        if (
                intervals_pupil[begin_with_pupil][1] > intervals_tutor[begin_with_tutor][0]
                and
                intervals_pupil[begin_with_pupil][0] < intervals_tutor[begin_with_tutor][1]
        ):
            appearance_time += (
                    min(intervals_pupil[begin_with_pupil][1], intervals_tutor[begin_with_tutor][1])
                    -
                    max(intervals_pupil[begin_with_pupil][0], intervals_tutor[begin_with_tutor][0])
            )

        if intervals_pupil[begin_with_pupil][1] <= intervals_tutor[begin_with_tutor][1]:
            begin_with_pupil += 1
        elif intervals_tutor[begin_with_tutor][1] < intervals_pupil[begin_with_pupil][1]:
            begin_with_tutor += 1
    return appearance_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [12, 100],
             'pupil': [1, 4, 6, 14, 19, 60, 90, 120],
             'tutor': [0, 4, 12, 100]},
    'answer': 53
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests, 1):         # enumerating begin with number 1
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'