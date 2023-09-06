

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_beggining = intervals["lesson"][0]
    lesson_end = intervals["lesson"][1]
    total_time = 0
    tutor = merge_intervals(intervals["tutor"])
    pupil = merge_intervals(intervals["pupil"])
    for tutor_start, tutor_end in zip(tutor[::2], tutor[1::2]):
        for pupil_start, pupil_end in zip(pupil[::2], pupil[1::2]):
            delta = min(tutor_end, pupil_end, lesson_end) - max(tutor_start, pupil_start, lesson_beggining)
            total_time += delta if delta > 0 else 0
    return total_time


def merge_intervals(intervals: list[int]) -> list[int]:
    merged_intervals: list = []
    for start, end in zip(intervals[::2], intervals[1::2]):
        merged = False
        for j in range(0, len(merged_intervals), 2):
            if (
                min(merged_intervals[j + 1], end)
                - max(merged_intervals[j], start)
                > 0
            ):
                merged = True
                if (
                    start >= merged_intervals[j]
                    and end >= merged_intervals[j + 1]
                ):
                    merged_intervals.append(merged_intervals[j + 1])
                    merged_intervals.append(end)
                elif (
                    start <= merged_intervals[j]
                    and end <= merged_intervals[j + 1]
                ):
                    merged_intervals.append(start)
                    merged_intervals.append(merged_intervals[j])
        if not merged:
            merged_intervals.append(start)
            merged_intervals.append(end)
    return merged_intervals