""" Решение третьей задачи. """


def appearance(intervals: dict[str, list[int]]) -> int:
    """ Подсчёт времени одновременного присутствия на уроке и учителя (может быть только один)
    и учеников (может быть несколько).

    :param intervals: Словарь таймстэмпов (присутствие, отсутствие) для урока, учителя, учеников.
    :return: Время одновременного присутствия на текущем уроке и учителя, и учеников.
    """

    # Маркер таймстэмпа урока
    LESSON: str = 'lesson'
    # Маркер таймстэмпа ученика
    PUPIL: str = 'pupil'
    # Маркер таймстэмпа учителя
    TUTOR: str = 'tutor'
    # Маркер входа в урок
    IN: str = 'in'
    # Маркер выхода с урока
    OUT: str = 'out'
    # Исходный словарь преобразуем в набор списков: список таймстэмпов ученика, список таймстэмпов учителя.
    # Элемент каждого списка является кортежем вида: (timestamp, 'pupil', 'in')
    # Т. е.,
    # первый элемент кортежа - таймстэмп,
    # второй - метка учителя (или ученика, или урока),
    # метка входа (или выхода)
    pupil: list[tuple] = [tuple([timestamp, PUPIL, IN if i % 2 == 0 else OUT])
                          for i, timestamp in enumerate(intervals[PUPIL])]
    tutor: list[tuple] = [tuple([timestamp, TUTOR, IN if i % 2 == 0 else OUT])
                          for i, timestamp in enumerate(intervals[TUTOR])]
    lesson: list[tuple] = [tuple([timestamp, LESSON, IN if i % 2 == 0 else OUT])
                          for i, timestamp in enumerate(intervals[LESSON])]

    # Объединение всех списков.
    pupil.extend(tutor)
    pupil.extend(lesson)
    # Сортировка объединённого списка по таймстэмпу.
    common: list[tuple[int, str, str]] = sorted(pupil, key=lambda pupil: pupil[0])

    # Флаги нахождения на уроке.
    lesson_in: bool = False
    tutor_in: bool = False
    # Количество присутствующих на уроке учеников.
    pupil_in: int = 0
    # И учитель, и ученик(и) на уроке.
    together: bool = False
    # Точка (таймстэмп) начала общего присутствия на уроке.
    start: int = 0
    # Количество времени, когда и учитель, и ученик присутствуют на уроке одновременно (накопитель).
    sum_time: int = 0

    for (timestamp, actor, action) in common:
        # Проход по общему отсортированному списку таймстэмпов
        match actor:
            case 'pupil':
                # Если таймстэмп ученика
                # Фиксируется его присутствие на уроке
                pupil_in += 1 if action == IN else -1
            case 'tutor':
                # Если таймстэмп учителя
                # Фиксируется его присутствие на уроке
                tutor_in = True if action == IN else False
            case 'lesson':
                # Если таймстэмп урока
                lesson_in = True if action == IN else False

        if (pupil_in and tutor_in and lesson_in) and not together:
            # Если и учитель, и ученик внезапно оказались на уроке (а до этого момента, кого-то из них не хватало.
            # Фиксирование момента их присутствия
            start = timestamp
            together = True
        elif not (pupil_in and tutor_in and lesson_in) and together:
            # Если до этого момента и учитель, и ученик присутствовали на уроке,
            # а тут кто-то из них вышел (или урок закончился).
            together = False
            # Суммирование накопленного совместного времени пребывания.
            sum_time += timestamp - start

    return sum_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
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
