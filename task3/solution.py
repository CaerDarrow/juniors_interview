def update_sequence_by_interval(time_sequence: list[int],
                                interval: list[int]) -> None:
    """Добавляем интервал к последовательности непересекающихся временных меток.
    Сама последовательность апдейтится.

    :param time_sequence: неубывающая последовательность непересекающихся временных меток
    :param interval: интервал времени, который нужно добавить к последовательности
    """
    interval_idx = [None, None]

    for idx, value in enumerate(time_sequence):
        if interval_idx[0] is None and interval[0] <= value:
            interval_idx[0] = idx
        if interval_idx[1] is None and interval[1] < value:
            interval_idx[1] = idx

    interval_idx[1] = len(time_sequence) if interval_idx[1] is None else interval_idx[1]
    interval_idx[0] = len(time_sequence) if interval_idx[0] is None else interval_idx[0]

    if interval_idx[1] % 2 == 0:
        time_sequence.insert(interval_idx[1], interval[1])

    del time_sequence[interval_idx[0]:interval_idx[1]]

    if interval_idx[0] % 2 == 0:
        time_sequence.insert(interval_idx[0], interval[0])


def normalize_sequence(raw_sequence: list[int],
                       crop_interval: list[int]) -> list[int]:
    """Приводим последовательность временных меток к последовательности
    неубываемых непересекающихся временных меток
    с учётом максимально и минимально возможного времени.

    :param raw_sequence: Входящая последовательность временных меток
    :param crop_interval: Минимальное и максимально допустимое время в одном листе
    :return: Неубывающая и непересекающаяся последовательность временных меток
    """
    merged_sequence = []

    for p_idx in range(0, len(raw_sequence), 2):
        update_sequence_by_interval(
            merged_sequence,
            raw_sequence[p_idx:p_idx + 2]
        )

    return [min(max(value, crop_interval[0]), crop_interval[1])
            for value in merged_sequence]


def appearance(intervals: dict[str, list[int]]) -> int:
    """ Подсчет общего проведенного на уровке времени ученика и учителя.
    :param intervals: словарь с интервалами
    :return: время общего присутствия ученика и учителя на уроке (в секундах)
    """
    pupil_seq = normalize_sequence(
        intervals['pupil'],
        intervals['lesson']
    )
    tutor_seq = normalize_sequence(
        intervals['tutor'],
        intervals['lesson']
    )

    idx_pupil, idx_tutor = 0, 0
    is_pupil_on, is_tutor_on = False, False

    prev_common_interval = None
    prev_common_from = 0
    common_counter = 0

    for idx in range(len(pupil_seq) + len(tutor_seq)):

        if idx_tutor == len(tutor_seq) or (idx_pupil != len(pupil_seq)
                                           and pupil_seq[idx_pupil] < tutor_seq[idx_tutor]):

            current_value = pupil_seq[idx_pupil]
            is_pupil_on = not is_pupil_on
            idx_pupil += 1

        else:
            current_value = tutor_seq[idx_tutor]
            is_tutor_on = not is_tutor_on
            idx_tutor += 1

        if prev_common_interval:
            common_counter += current_value - prev_common_from
            prev_common_interval = False

        if is_pupil_on and is_tutor_on:
            prev_common_interval = True
            prev_common_from = current_value

    return common_counter
