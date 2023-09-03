def appearance(intervals: dict[str, list[int]]) -> int:
    """Counts common time in seconds which pupil and tutor were on lesson."""
    lesson_start, lesson_end = intervals['lesson']
    lesson_time = set(range(lesson_start, lesson_end))  # set of timestamps seconds of lesson

    pupil_intervals_ranges = [range(intervals['pupil'][i], intervals['pupil'][i+1]) for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals_ranges = [range(intervals['tutor'][i], intervals['tutor'][i+1]) for i in range(0, len(intervals['tutor']), 2)]

    pupil_time = set().union(*pupil_intervals_ranges)  # set of timestamps seconds of pupil presence on lesson
    tutor_time = set().union(*tutor_intervals_ranges)  # set of timestamps seconds of tutor presence on lesson
    common_time = lesson_time & pupil_time & tutor_time
    return len(common_time)
