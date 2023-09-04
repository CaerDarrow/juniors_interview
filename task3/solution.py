def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_beggining = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]
    total_time = 0
    tutor = normalize_intervals(intervals['tutor'])
    pupil = normalize_intervals(intervals['pupil'])
    for i in range(0, len(tutor), 2):
        for j in range(0, len(pupil), 2):
            delta = min(tutor[i+1], pupil[j+1], lesson_end) - max(tutor[i], pupil[j], lesson_beggining) 
            total_time += delta if delta > 0 else 0
    return total_time


def normalize_intervals(intervals):
    normalized_intervals = []
    for i in range(0, len(intervals), 2):
        applied = False
        for j in range(0, len(normalized_intervals), 2):
            if min(normalized_intervals[j+1], intervals[i+1]) - max(normalized_intervals[j], intervals[i]) > 0:
                applied = True
                if intervals[i] >= normalized_intervals[j] and intervals[i+1] >= normalized_intervals[j+1]:
                    normalized_intervals.append(normalized_intervals[j+1])
                    normalized_intervals.append(intervals[i+1])
                elif intervals[i] <= normalized_intervals[j] and intervals[i+1] <= normalized_intervals[j+1]:
                    normalized_intervals.append(intervals[i])
                    normalized_intervals.append(normalized_intervals[j])
        if not applied:
            normalized_intervals.append(intervals[i])
            normalized_intervals.append(intervals[i+1])
    return normalized_intervals



