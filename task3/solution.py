from Exceptions import ListOddLength

def intersection(lesson: list[int], pupil: list[int], tutor: list[int]) -> list[list[int]]:
    start_lesson, end_lesson = lesson[0], lesson[1]
    i, j = 0, 0

    overlaps = []
    while i < len(pupil) and j < len(tutor):
        start_intersection = max(start_lesson, pupil[i], tutor[j])
        end_entersection = min(end_lesson, pupil[i + 1], tutor[j + 1])

        if start_intersection <= end_entersection:
            overlaps.append([start_intersection, end_entersection])
        if pupil[i + 1] < tutor[j + 1]:
            i += 2
        else:
            j += 2

    return overlaps

def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged = []
    for i in range(len(intervals)):
        if merged and merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged

def appearance(intervals: dict[str, list[int]]) -> int:
    if len(intervals['pupil']) % 2 != 0:
        raise ListOddLength('pupil')
    if len(intervals['tutor']) % 2 != 0:
        raise ListOddLength('tutor')
     
    merged = merge(intersection(intervals['lesson'], intervals['pupil'], intervals['tutor']))

    return sum(end - start for start, end in merged)
