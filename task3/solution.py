def get_sum(intervals: list[int]) -> int:
    total_sum = 0
    for i, seconds in enumerate(intervals):
        if i % 2 == 0:
            total_sum -= seconds
            continue

        total_sum += seconds

    return total_sum


def correct_intervals(
        limits: list[int],
        intervals: list[int]
) -> list[int]:
    result = []
    for i in range(0, len(limits), 2):
        start = limits[i]
        end = limits[i + 1]
        for j in range(0, len(intervals), 2):
            i_start = intervals[j]
            i_end = intervals[j + 1]

            left = max(start, i_start)
            right = min(end, i_end)

            if left >= right:
                continue

            if result and left <= result[-1]:
                result[-1] = max(result[-1], right)
            else:
                result.extend([left, right])

    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    tutor = correct_intervals(intervals['lesson'], intervals['tutor'])
    pupil = correct_intervals(tutor, intervals['pupil'])

    return get_sum(pupil)


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
    for index, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test[
            'answer'], f'Error on test case {index}, got {test_answer}, expected {test["answer"]}'

        print(f'Error on test case {index}, got {test_answer}, expected {test["answer"]}')
