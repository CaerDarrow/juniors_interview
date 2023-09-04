def get_time_intervals(items: list[int]) -> set:
    result = set()
    for i in range(0, len(items), 2):
        result = result | {s for s in range(items[i], items[i + 1])}
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    results = []
    for item in intervals:
        results.append(get_time_intervals(intervals[item]))
    answer = len(results[0] & results[1] & results[2])
    print(f"{answer//3600}:{answer//60%60}:{answer%60} or ({answer} second)")
    return answer


lesson_1 = {
        'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                  1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                  1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                  1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                  1594706524, 1594706524, 1594706579, 1594706641],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
    }


appearance(lesson_1)
