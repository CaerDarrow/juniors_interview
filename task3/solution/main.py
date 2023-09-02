def appearance(intervals):
    total_pupil_time = 0
    total_tutor_time = 0
    
    for i in range(0, len(intervals['pupil']) - 1, 2):
        print(intervals['pupil'][i + 1] - intervals['pupil'][i] , intervals['pupil'][i + 1], intervals['pupil'][i] )
        total_pupil_time += intervals['pupil'][i + 1] - intervals['pupil'][i] 

    for i in range(0, len(intervals['tutor']) - 1, 2):

        total_tutor_time += intervals['tutor'][i + 1] - intervals['tutor'][i] 

    total_time =  (total_pupil_time + total_tutor_time)
    return total_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [2800, 6400],
                   'pupil': [2789, 4500, 2807, 4542, 4512, 4513, 4564,
                             5150, 4581, 4582, 4734, 5009, 5095, 5096,
                             5106, 6480, 5158, 5773, 5849, 6480, 6500,
                             6875, 6502, 6503, 6524, 6524, 6579, 6641],
                   'tutor': [35, 364, 2749, 5148, 5149, 6463]},
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
        print(test_answer, test['answer'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
