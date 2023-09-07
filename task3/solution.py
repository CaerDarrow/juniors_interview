'''Доброго времени суток! Есть вопросы по заданию:
1) Не совсем понятна фраза "общее количество секунд на уроке ученика и преподавателя".
Понял, как среднее арифметическое. 
2) Судя по цифрам захода и выхода, урок посещает не один ученик, 
поэтому, чтобы получить общую цифру, так же посчитал среднее арифметическое'''
def appearance(intervals: dict[str, list[int]]) -> int:
    pupils_seconds = intervals.get('pupil')
    tutor_seconds = intervals.get('tutor')
    lesson_seconds = intervals.get('lesson')
    p_length = len(pupils_seconds)
    t_length = len(tutor_seconds)
    pupil_time = []
    tutor_time = []
    for i in range(0,p_length):
        if i%2!=0:
            if pupils_seconds[i] <=lesson_seconds[1] and pupils_seconds[i-1]>=lesson_seconds[0]: #Зашел позже, ушел раньше
                pupil_time.append(pupils_seconds[i]-pupils_seconds[i-1])
            elif pupils_seconds[i-1]<lesson_seconds[0] and pupils_seconds[i]<=lesson_seconds[1]: #Зашел раньше, ушел раньше
                pupil_time.append(pupils_seconds[i]-lesson_seconds[0])
            elif pupils_seconds[i-1]>=lesson_seconds[0] and pupils_seconds[i]>=lesson_seconds[1]: #Зашел позже, ушел позже (исключение - зашел позже конца урока)
                positive_checker = lesson_seconds[1] - pupils_seconds[i-1]
                if positive_checker>0:
                    pupil_time.append(positive_checker)
            elif pupils_seconds[i-1]<=lesson_seconds[0] and pupils_seconds[i]>=lesson_seconds[1]: #Зашел раньше, ушел позже
                pupil_time.append(lesson_seconds[1]- lesson_seconds[0])
            else: 
                break
    for j in range(0,t_length):
        if j%2!=0:
            if tutor_seconds[j]<=lesson_seconds[1] and tutor_seconds[j-1]>=lesson_seconds[0]: #Зашел позже, ушел раньше
                tutor_time.append(tutor_seconds[j]-tutor_seconds[j-1])
            elif tutor_seconds[j-1]<lesson_seconds[0] and tutor_seconds[j]<=lesson_seconds[1]: #Зашел раньше, ушел раньше(исключение - зашел и ушел раньше начала урока)
                positive_checker = tutor_seconds[j]-lesson_seconds[0]
                if positive_checker>0:
                    tutor_time.append(positive_checker)
            elif tutor_seconds[j-1]>=lesson_seconds[0] and tutor_seconds[j]>=lesson_seconds[1]: #Зашел позже, ушел позже
                tutor_time.append(lesson_seconds[1]-tutor_seconds[j-1])
            elif tutor_seconds[j-1]<=lesson_seconds[0] and tutor_seconds[j]>=lesson_seconds[1]: #Зашел раньше, ушел позже
                tutor_time.append(lesson_seconds[1]-lesson_seconds[0])
            else:
                break
    p_digit = 0 #количество секунд посещения ученика
    t_digit = 0 #количество секунд посещения преподавателя
    for p in pupil_time:
        p_digit+=p
    for t in tutor_time:
        t_digit+=t
    half_of_list_seconds = p_length/2
    p_digit = p_digit/half_of_list_seconds #среднее количество секунд на всех учеников
    all_time = round((p_digit + t_digit)/2) #общее количество секунд на учеников и преподавателя
    return all_time
            

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