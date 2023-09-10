from solution import appearance

tests_base = [
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

my_tests = [
    {'intervals': {'lesson': [100, 200],
     'pupil': [100, 101, 150, 150, 160, 180],
     'tutor': [0, 98, 99, 120, 170, 173, 179, 220]},
    'answer': 5},
    {'intervals': {'lesson': [897, 1230],
     'pupil': [100, 800, 850, 900, 1000, 1230, 1225, 1231, 1000, 1100, 1050, 1121],
     'tutor': [700, 1229, 1230, 1231]},
    'answer': 232},
    {'intervals': {'lesson': [10000, 12201],
     'pupil': [10030, 10200, 10031, 100800, 11000, 11100, 11050, 11341, 11340, 11567, 11800, 12200],
     'tutor': [9950, 10500, 10600, 10999, 11200, 12303]},
    'answer': 1870},
    {'intervals': {'lesson': [10047, 13720],
     'pupil': [10056, 10080, 10200, 10240],
     'tutor': [9000, 10000, 10035, 10050]},
    'answer': 0},
    {'intervals': {'lesson': [21345, 25324],
     'pupil': [21799, 21900],
     'tutor': [19400, 20000, 20020, 21200]},
    'answer': 0},
    {'intervals': {'lesson': [21345, 25324],
     'pupil': [21799, 21900],
     'tutor': []},
    'answer': 0},
    {'intervals': {'lesson': [21345, 25324],
     'pupil': [],
     'tutor': [21345, 21700]},
    'answer': 0},
    {'intervals': {'lesson': [21345, 25324],
     'pupil': [],
     'tutor': []},
    'answer': 0},
]

if __name__ == '__main__':
   for i, test in enumerate(tests_base):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
   for i, test in enumerate(my_tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'