def appearance(intervals: dict[str, list[int]]) -> int:
    # Переводим все интервалы с сессиями в сеты диапазонов, будем искать пересечение
    # Берём за основу временной интервал урока
    lesson_set = set(range(intervals['lesson'][0], intervals['lesson'][1]))

    pupil_set = set()
    tutor_set = set()

    # Добавляем в сеты диапазоны с учеником и учителем
    for i in range(0, len(intervals['pupil']), 2):
        pupil_set.update(set(range(intervals['pupil'][i], intervals['pupil'][i + 1])))

    for i in range(0, len(intervals['tutor']), 2):
        tutor_set.update(set(range(intervals['tutor'][i], intervals['tutor'][i + 1])))

    # Теперь находим время, когда и учитель и ученик одновременно присутствовали на уроке, это пересечение трех сетов
    intersection_time = lesson_set.intersection(pupil_set, tutor_set)

    # Возвращаем количество секунд одновременного присутствия
    return len(intersection_time)