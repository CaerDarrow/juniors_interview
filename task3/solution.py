def arrange_intervals(intervals: list) -> list:
    normal_list = list()
    it = iter(intervals)
    intervals = list(zip(it, it))
    intervals.sort(key=lambda x: x[0])
    for start, end in intervals:
        if len(normal_list) == 0:
            normal_list.append(start)
            normal_list.append(end)
        if start < normal_list[-1] and end < normal_list[-1]:
            continue
        if start < normal_list[-1]  and end > normal_list[-1]:
            normal_list.append(normal_list[-1])
            normal_list.append(end)
        if  normal_list[-1] < start  and  normal_list[-1] < end:
            normal_list.append(start)
            normal_list.append(end)
    return normal_list

def appearance(intervals: dict[str, list[int]]) -> int:
    position, summ_time = 0, 0
    iter_list = arrange_intervals(intervals["pupil"])
    check_list = arrange_intervals(intervals["tutor"])
    if len(check_list) > len(iter_list):
        iter_list, check_list = check_list, iter_list
    for index_iter, timestamp_iter in enumerate(iter_list):
        if index_iter % 2 != 0:
            continue
        start_time_iter, end_time_iter = timestamp_iter, iter_list[index_iter + 1]
        if start_time_iter < intervals["lesson"][0]:
            start_time_iter = intervals["lesson"][0]
        if end_time_iter > intervals["lesson"][1]:
            end_time_iter = intervals["lesson"][1]
        for index_check, timestamp_check in enumerate(check_list):
            if index_check  % 2 != 0:
                continue
            start_time_check, end_time_check = timestamp_check, check_list[index_check + 1]
            if  start_time_iter < start_time_check and end_time_check < iter_list[index_check + 1]:
                summ_time += end_time_check - check_list[index_check]
                position = index_check + 2
            elif  start_time_check < start_time_iter and  end_time_check < end_time_iter and start_time_iter < end_time_check:
                summ_time += end_time_check - start_time_iter
                position = index_check + 2
            elif start_time_iter < start_time_check and end_time_iter < end_time_check and start_time_check < end_time_iter:
                summ_time += end_time_iter - start_time_check
            elif start_time_check < start_time_iter and iter_list[index_check + 1] < end_time_check:
                summ_time += end_time_iter - start_time_iter
        check_list = check_list[position:]
    return summ_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117 
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'