def appearance(intervals: dict[str, list[int]], existing_answer: int) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']
    
    total_presence = 0
    
    for i in range(0, len(pupil_intervals), 2):
        pupil_entry, pupil_exit = pupil_intervals[i], pupil_intervals[i + 1]
        
        for j in range(0, len(tutor_intervals), 2):
            tutor_entry, tutor_exit = tutor_intervals[j], tutor_intervals[j + 1]
            
            overlap_start = max(pupil_entry, tutor_entry, lesson_start)
            overlap_end = min(pupil_exit, tutor_exit, lesson_end)
            
            if overlap_start < overlap_end:
                total_presence += overlap_end - overlap_start

    assert existing_answer == total_presence, f'Error on test case {i}, got {total_presence}, expected {existing_answer}'
    return total_presence
