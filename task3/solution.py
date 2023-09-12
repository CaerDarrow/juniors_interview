def create_intervals(x1: int, x2: int, l: list[int]) -> list[tuple[int]]:
    total = list()

    for i in range(0, len(l), 2):
        y1, y2 = l[i], l[i + 1]
        if y1 < x1:
            y1 = x1
        elif x2 < y2:
            y2 = x2
        total.append((y1, y2))

    return total

def calculate_total_intersection(l1, l2):
    total_intersection = 0

    for start1, end1 in l1:
        for start2, end2 in l2:
            intersection_start = max(start1, start2)# пересечение между интервалами
            intersection_end = min(end1, end2)

            if intersection_start < intersection_end:# есть ли пересечение
                total_intersection += intersection_end - intersection_start

    return total_intersection

def merge_intervals(intervals):
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:# есть ли пересечение между текущим и предыдущим интервалами
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)# если нет добавляем текущий интервал в объединенный список
    return merged


def appearance(intervals: dict[str, list[int]]) -> int:
    list_pup, list_tut = intervals['pupil'], intervals['tutor']
    x1, x2 = intervals['lesson']
    l1 = create_intervals(x1, x2, list_pup)
    l2 = create_intervals(x1, x2, list_tut)
    inv1, inv2 = merge_intervals(l1), merge_intervals(l2)
    return calculate_total_intersection(inv1, inv2)

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                       1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009,
                       1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480,
                       1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
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
