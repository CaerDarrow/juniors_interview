def common_sessions(first_session: list, second_session: list) -> list:
    """Функция определяет промежутки вхождений вторых интервалов в первые"""
    common_sessions = []
    for sec_num, sec_session in enumerate(second_session):
        if sec_num % 2 == 0:
            for fst_num, fst_session in enumerate(first_session):
                if fst_num % 2 == 0 and sec_session <= first_session[fst_num + 1]:
                    if second_session[sec_num + 1] >= fst_session:
                        # Есть вхождение, проверяем начало
                        common_sessions.append(max(fst_session, sec_session))
                        #Теперь проверяем окончание
                        if second_session[sec_num + 1] <= first_session[fst_num + 1]:
                            common_sessions.append(second_session[sec_num + 1])
                        else:
                            common_sessions.append(first_session[fst_num + 1])
    return common_sessions


def count_time(intervals: list) -> int:
    """подсчет секунд"""
    count_set = set()
    for num, interval in enumerate(intervals):
        if num % 2 == 0:
            number = interval
            while number != intervals[num+1]:
                count_set.add(number)
                number += 1
    counter = len(count_set)
    return counter


def appearance(intervals: dict[str, list[int]]) -> int:
    common_intervals = common_sessions(intervals.get('lesson'), intervals.get('pupil'))
    common_intervals = common_sessions(intervals.get('tutor'), common_intervals)
    counter = count_time(common_intervals)
    return counter



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

