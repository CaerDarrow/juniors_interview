def merge_intervals(interval_list: list[int]) -> list[int]:
    """Merges overlapping intervals inside a list."""
    result = [interval_list[0], interval_list[1]] if interval_list else []
    # Using 2 pointers technique
    left = right = 0

    for right in range(2, len(interval_list), 2):
        # Intervals considered overlapping if next interval starts before current one ends
        if interval_list[right] < result[left+1]:
            # Merging intervals
            result[left + 1] = max(result[left+1], interval_list[right+1])
        else:

            result.extend(interval_list[right:right+2])
            left += 2

    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    """Returns amount of time that student and tutor were online simultaneously during the lesson."""
    simultaneous_online_time = 0
    lesson_start, lesson_end = intervals.get('lesson')
    student_intervals = merge_intervals(intervals.get('pupil'))
    tutor_intervals = merge_intervals(intervals.get('tutor'))
    i = j = 0

    while i < len(student_intervals) and j < len(tutor_intervals):
        student_interval_start, student_interval_end = student_intervals[i:i+2]
        tutor_interval_start, tutor_interval_end = tutor_intervals[j:j+2]

        # Handling non-overlapping intervals
        if student_interval_end < tutor_interval_start:
            i += 2
        elif tutor_interval_end < student_interval_start:
            j += 2
        else:
            # Handling overlap
            overlap_start = max(lesson_start, student_interval_start, tutor_interval_start)
            overlap_end = min(lesson_end, student_interval_end, tutor_interval_end)
            simultaneous_online_time += max(0, overlap_end - overlap_start)

            # Switching to the next interval
            if student_interval_end < tutor_interval_end:
                i += 2
            else:
                j += 2

    return simultaneous_online_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },

    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },

    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },

    # Added test case if student didn't appear.
    {'intervals': {'lesson': [1594666800, 1594670400],
                   'pupil': [],
                   'tutor': [1594666920, 1594667080]},
     'answer': 0
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'


