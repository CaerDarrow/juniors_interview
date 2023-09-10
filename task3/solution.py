def filter_time_lesson(intervals: list[list[int]], lesson: list[int]) -> list[list[int]]:
    filter_intervals = []
    start_lesson, end_lesson = lesson
    for interval in intervals:
        start_pupil, end_pupil = interval
        if not (start_pupil >= end_lesson or end_pupil <= start_lesson):
            filter_intervals.append([max(start_lesson, interval[0]), min(end_lesson, interval[1])])
    return filter_intervals


def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    cur, res = 0, []
    while cur != len(intervals) and intervals[cur][1] < new_interval[0]:
        res.append(intervals[cur])
        cur += 1
    while cur != len(intervals) and new_interval[1] >= intervals[cur][0]:
        new_interval[0] = min(intervals[cur][0], new_interval[0])
        new_interval[1] = max(intervals[cur][1], new_interval[1])
        cur += 1
    res.append(new_interval)
    for j in range(cur, len(intervals)):
        res.append(intervals[cur])
    return res


def conversion_intervals(list_times: list[int], lesson: list[int]) -> list[list[int]]:
    list_intervals = []
    for j in range(0, len(list_times), 2):
        list_intervals.append([list_times[j], list_times[j + 1]])
    filter_list_intervals = filter_time_lesson(list_intervals, lesson)
    all_union_intervals = []
    for interval in filter_list_intervals:
        all_union_intervals = insert_interval(all_union_intervals, interval)
    return all_union_intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    list_tutor, list_pupil = intervals['tutor'], intervals['pupil']
    common_seconds = 0
    intervals_tutor, intervals_pupil = [conversion_intervals(list_tutor, intervals['lesson']),
                                        conversion_intervals(list_pupil, intervals['lesson'])]
    cur_pos_tutor, cur_pos_pupil = 0, 0

    while cur_pos_tutor != len(intervals_tutor) and cur_pos_pupil != len(intervals_pupil):
        tutor_start, tutor_end = intervals_tutor[cur_pos_tutor]
        pupil_start, pupil_end = intervals_pupil[cur_pos_pupil]
        if pupil_end >= tutor_start and pupil_start <= tutor_end:
            result = min(tutor_end, pupil_end) - max(tutor_start, pupil_start)
            common_seconds += result
        if tutor_end > pupil_end:
            cur_pos_pupil += 1
        else:
            cur_pos_tutor += 1

    return common_seconds
