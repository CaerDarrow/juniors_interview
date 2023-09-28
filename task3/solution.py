def fix_intervals(pupil_or_tutor: list[int], start_lesson: int, end_lesson: int) -> None:
    for i in range(len(pupil_or_tutor)):
        if pupil_or_tutor[i] < start_lesson:
            pupil_or_tutor[i] = start_lesson
        elif pupil_or_tutor[i] > end_lesson:
            pupil_or_tutor[i] = end_lesson


def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson, end_lesson = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]

    fix_intervals(pupil, start_lesson, end_lesson)
    fix_intervals(tutor, start_lesson, end_lesson)

    start = tutor[0]
    result_sec = 0

    for i in range(0, len(tutor), 2):
        for j in range(0, len(pupil), 2):
            if start < pupil[j+1]:
                x = max(tutor[i], pupil[j])
                y = min(tutor[i+1], pupil[j+1])

                if x > y:
                    continue
                if x > start:
                    start = x

                result_sec += y - start
                start = y

    return result_sec


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