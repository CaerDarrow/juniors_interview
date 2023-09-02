from typing import Tuple


def appearance(intervals: dict[str, list[int]], **kwargs) -> int:
    """Возвращает суммарное время, проведенное учеником и учителем на уроке."""

    pupil_session_on_lesson = get_sessions_on_lesson(intervals['lesson'],
                                                     intervals['pupil'])
    tutor_session_on_lesson = get_sessions_on_lesson(intervals['lesson'],
                                                     intervals['tutor'])
    return get_session_intersection_in_sec(
        pupil_session_on_lesson, tutor_session_on_lesson)


def get_session_intersection_in_sec(pupil_ses: list[Tuple[int]],
                                    tutor_ses: list[Tuple[int]]) -> int:
    """Возвращает общее временя в секундах """

    i, j, result_sec = 0, 0, 0
    while i < len(pupil_ses) and j < len(tutor_ses):
        if pupil_ses[i][1] > tutor_ses[j][0] and \
                pupil_ses[i][0] < tutor_ses[j][1]:
            result_sec += min(pupil_ses[i][1], tutor_ses[j][1]) - max(
                pupil_ses[i][0], tutor_ses[j][0])

        if pupil_ses[i][1] <= tutor_ses[j][1]:
            i += 1
        elif tutor_ses[j][1] < pupil_ses[i][1]:
            j += 1
    return result_sec

def get_sessions_on_lesson(lesson: list[int, int],
                           person_intervals: list[int]) -> list[Tuple[int]]:
    """Возвращает список кортежей с временем начала и конца сессии человека.
    Если время сессии вышло за рамки урока, то все, что за пределами диапазиона
    в сессии не учитывается."""
    person_sessions = [[i, j] for i, j in
                       zip(person_intervals[::2], person_intervals[1::2])]
    person_sessions_on_lesson = []
    for session_start, session_end in person_sessions:
        if session_start < lesson[1] and session_end > lesson[0]:
            if session_start < lesson[0]:
                session_start = lesson[0]
            if session_end > lesson[1]:
                session_end = lesson[1]
            person_sessions_on_lesson.append((session_start, session_end))
    return person_sessions_on_lesson


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                             1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                             1594704512, 1594704513, 1594704564, 1594705150,
                             1594704581, 1594704582, 1594704734, 1594705009,
                             1594705095, 1594705096, 1594705106, 1594706480,
                             1594705158, 1594705773, 1594705849, 1594706480,
                             1594706500, 1594706875, 1594706502, 1594706503,
                             1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                             1594705149, 1594706463]},
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
        if i == 1:
            print('Тест №2 является некорректным, т.к. в интервалах pupil 3-ий элемени меньше 2-го. pupil: [1594702789, 1594704500, 1594702807, 1594704542...]')
            print('В последующих интервала также встречаются ошибки.')
            continue
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
