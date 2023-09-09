def appearance(intervals):
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    time_together = 0

    for i in range(0, len(pupil_intervals), 2):
        pupil_connect = pupil_intervals[i]
        pupil_disconnect = pupil_intervals[i + 1]

        for j in range(0, len(tutor_intervals), 2):
            tutor_connect = tutor_intervals[j]
            tutor_disconnect = tutor_intervals[j + 1]

            common_start = max(pupil_connect, tutor_connect, lesson_start)
            common_end = min(pupil_disconnect, tutor_disconnect, lesson_end)

            if common_start < common_end:
                time_together += common_end - common_start

    return time_together
