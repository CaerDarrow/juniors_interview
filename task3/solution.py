from itertools import chain, cycle


def marked_events(events):
    "Маркировка начала и окончания событий."
    yield from zip(events, cycle((-1, 1)))


def union_events(events):
    "Объединение массива событий."
    balance = 0
    for time, status_point in sorted(marked_events(events)):
        balance += status_point
        if (
            balance == -1 and status_point == -1 or
            balance == 0 and status_point == 1
        ):
            yield time, status_point


def intersect_marked_events(*many_group_events):
    "Пересечение маркированного массива событий."
    events = sorted(chain(*many_group_events))
    start_event = - len(many_group_events)
    end_event = start_event + 1
    count_marked_pred_status = 0
    for time, status_point in events:
        count_marked_next_status = count_marked_pred_status + status_point
        if (
            count_marked_pred_status == end_event and
            count_marked_next_status == start_event or
            count_marked_pred_status == start_event and
            count_marked_next_status == end_event
        ):
            yield time, status_point
        count_marked_pred_status = count_marked_next_status


def appearance(intervals: dict[str, list[int]]) -> int:
    "Возвращает время общего присутствия ученика и учителя на уроке (в секундах)."
    lesson = marked_events(intervals['lesson'])
    pupil = union_events(intervals['pupil'])
    tutor = union_events(intervals['tutor'])
    return sum(
        time * status_point
        for time, status_point in intersect_marked_events(lesson, pupil, tutor)
    )
