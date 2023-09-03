from intervals_data import tests


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    pupil_presence_timestamps = _generate_timestamp_set(intervals=pupil_intervals)
    tutor_presence_timestamps = _generate_timestamp_set(intervals=tutor_intervals)

    common_presence_timestamps = pupil_presence_timestamps.intersection(tutor_presence_timestamps)
    lesson_time_timestamps = range(lesson_start, lesson_end)

    total_presence_timestamps = common_presence_timestamps.intersection(lesson_time_timestamps)
    result = len(total_presence_timestamps)

    return result


def _generate_timestamp_set(intervals: list[int]) -> set[range]:
    result = set()

    for lesson_enter_id in range(0, len(intervals), 2):
        lesson_exit_id = lesson_enter_id + 1

        range_between_enter_and_exit = range(intervals[lesson_enter_id], intervals[lesson_exit_id])
        result.update(range_between_enter_and_exit)

    return result


if __name__ == '__main__':
    for i, test in enumerate(tests, start=1):
        test_answer = appearance(test['intervals'])
        expected_answer = test['answer']

        assert test_answer == expected_answer, f'Error on test case {i}, got {test_answer}, expected {expected_answer}'
