def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson'][0], intervals['lesson'][1] 
    pupil = [(event, 1 - 2 * (i % 2), 'pupil') for i, event in enumerate(intervals['pupil'])]
    tutor = [(event, 1 - 2 * (i % 2), 'tutor') for i, event in enumerate(intervals['tutor'])]
    events = pupil + tutor
    events.sort()
    for i, elem in enumerate(events):
        event, startend, role = elem
        if event < lesson_start:
            events[i] = (lesson_start, startend, role)
        if event > lesson_end:
            events[i] = (lesson_end, startend, role)
    pupil_count = 0
    tutor_count = 0
    temp = -1
    total_time = 0
    for event, startend, role in events:
        if role == 'pupil':
            pupil_count += startend
        else:
            tutor_count += startend
        if pupil_count > 0 and tutor_count > 0 and temp == -1:
            temp = event
        if (pupil_count < 1 or tutor_count < 1) and temp != -1:
            total_time += event - temp
            temp = -1
    return total_time