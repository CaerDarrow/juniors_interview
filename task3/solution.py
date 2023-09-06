def appearance(intervals):
    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = [(intervals['pupil'][i], intervals['pupil'][i + 1]) for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [(intervals['tutor'][i], intervals['tutor'][i + 1]) for i in range(0, len(intervals['tutor']), 2)]

    pupil_time = set(time for start, end in pupil_intervals for time in range(start, end))
    tutor_time = set(time for start, end in tutor_intervals for time in range(start, end))

    common_time = pupil_time & tutor_time & set(range(lesson_start, lesson_end))

    return len(common_time)
