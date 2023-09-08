def appearance(intervals: dict[str, list[int]]) -> int:
    minimum = intervals['lesson'][0]
    maximum = intervals['lesson'][1]
    intervals['pupil'] = list(map(lambda i: ((i - minimum) if (i - minimum) > 0 else 0) if i < maximum else maximum - minimum, intervals['pupil']))
    intervals['tutor'] = list(map(lambda i: ((i - minimum) if (i - minimum) > 0 else 0) if i < maximum else maximum - minimum, intervals['tutor']))
    pupil_list = []
    for i in range(int(len(intervals['pupil'])/2)):
        start_i = intervals['pupil'][i*2]
        end_i = intervals['pupil'][i*2+1]
        if len(pupil_list) == 0:
            pupil_list.append([start_i, end_i])
        else:
            flag = True
            for j in pupil_list:
                if start_i <= j[1]:
                    j[0] = min(j[0], start_i)
                    j[1] = max(j[1], end_i)
                    flag = False
                    break
            if flag:
                pupil_list.append([start_i, end_i])
    tutor_list = []
    for i in range(int(len(intervals['tutor'])/2)):
        start_i = intervals['tutor'][i*2]
        end_i = intervals['tutor'][i*2+1]
        if len(tutor_list) == 0:
            tutor_list.append([start_i, end_i])
        else:
            flag = True
            for j in tutor_list:
                if start_i <= j[1]:
                    j[0] = min(j[0], start_i)
                    j[1] = max(j[1], end_i)
                    flag = False
                    break
            if flag:
                tutor_list.append([start_i, end_i])
    intervals['pupil'] = pupil_list
    intervals['tutor'] = tutor_list

    interval_summ = 0
    for i in intervals['pupil']:
        start_i = i[0]
        end_i = i[1]
        for j in intervals['tutor']:
            start_j = j[0]
            end_j = j[1]
            if end_i <= start_j:
                pass
            elif start_i >= end_j:
                pass
            else:
                start = max(start_i, start_j)
                end = min(end_i, end_j)
                interval_summ += (end - start)
    return interval_summ


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
