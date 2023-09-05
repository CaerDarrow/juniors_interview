def interval(interval: list[int]) -> list[int]:
    copy = []
    for i in range(0, len(interval), 2):
        copy.append((interval[i], interval[i + 1]))
    copy.sort(key=lambda x: x[0])
    example = [copy[0][0], copy[0][1]]

    if len(copy) > 1:
        for i in range(1, len(copy)):
            left, right = copy[i]
            one = 1
            while one <= len(example) - 1:
                if left <= example[one] < right:
                    example[one] = right
                    break
                if left <= example[one] and right <= example[one]:
                    break
                else:
                    one += 2
            else:
                example += [left, right]

    return example


def appearance(intervals: dict[str, list[int]]) -> int:
    start, end = intervals.get('lesson')
    pupil = interval(intervals.get('pupil'))
    tutor = interval(intervals.get('tutor'))
    total = 0
    zero, one = 0, 0
    while zero < len(tutor) - 1 and one < len(pupil) - 1:
        start_pupil, end_pupil = pupil[one], pupil[one + 1]
        start_tutor, tutor_end = tutor[zero], tutor[zero + 1]
        left = max(start_pupil, start_tutor)
        right = min(end_pupil, tutor_end)
        if right > left:
            range = [max(start_pupil, start_tutor), min(end_pupil, tutor_end)]
            if range[0] < start < range[1]:
                range[0] = start
            if range[0] < end < range[1]:
                range[1] = end
            if range[0] >= start and range[1] <= end:
                total += range[1] - range[0]
        if end_pupil < tutor_end:
            one += 2
        else:
            zero += 2
    return total


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
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
