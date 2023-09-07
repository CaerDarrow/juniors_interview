from itertools import chain


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Данная функция получает на вход словарь с ключами *'lesson'*, *'tutor'* и *'pupil'*, значения которых являются
    списками с таймстемпами (время в секундах):\n
    lesson – начало и конец урока, pupil – интервалы присутствия ученика, tutor – интервалы присутствия учителя\n
    Интервалы устроены следующим образом – это всегда список из четного количества элементов.
    Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
    Функция возвращает время общего присутствия ученика и учителя на уроке (в секундах).
        **Attributes**:
            intervals: Словарь с таймстепами\n
    """
    pupil_intervals = intervals.get('pupil')
    tutor_intervals = intervals.get('tutor')
    lesson_intervals = intervals.get('lesson')
    # Проверяем на наличие пустых или непереданных списков тайстемпов
    if None in (pupil_intervals, tutor_intervals, lesson_intervals):
        raise KeyError('Не хватает входных таймстемпов')
    if not (lesson_intervals and tutor_intervals and pupil_intervals):
        return 0

    # Получаем все временные метки урока, т.е. если интервал урока 1,2,3,4,5....10000
    # мы получаем set{1,2,3,4,5......9999}
    summary_time = set(tuple(range(lesson_intervals[0], lesson_intervals[1])))

    # получаем интервалы присутствия ученика и тютора, создавая range из времени когда они заходили и выходили,
    # после конвертируя ренжи в кортежи всех значений внутри ренжей и объединив кортежи в чеине
    pupil_intervals_summary = chain.from_iterable(tuple(range(pupil_intervals[i], pupil_intervals[i + 1]))
                                                       for i in range(0, len(pupil_intervals), 2))
    tutor_intervals_summary = chain.from_iterable(tuple(range(tutor_intervals[i], tutor_intervals[i + 1]))
                                                       for i in range(0, len(tutor_intervals), 2))

    # конвертируем полученные метки присутствия ученика и учителя и выполняем операцию пересечения между
    # временем урока, временем присутствия ученика и учителя, на выходе получаем метки присутствия ученика и учителя во время урока
    summary_time.intersection_update(set(pupil_intervals_summary) & set(tutor_intervals_summary))

    # возвращаем количество этих меток, так как каждая метка это секунда, то их общее количество есть
    # время совместное присутствия ученика и учителя на уроке
    return len(summary_time)