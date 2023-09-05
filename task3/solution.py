class Interval(tuple):
    def __new__(cls, a: tuple):
        return super(Interval, cls).__new__(cls, a)

    def __init__(self, a: tuple):
        self._range = range(a[0], a[1])

    def range(self) -> range:
        return self._range


def appearance(intervals: dict[str, list[int]]) -> int:
    seconds = []
    lesson_interval = Interval(tuple(intervals['lesson']))
    # create list of pupil intervals
    pupil_iter = iter(intervals['pupil'])
    pupil_tuples = zip(pupil_iter, pupil_iter)
    pupil_intervals = [Interval(tup) for tup in pupil_tuples]
    # create list of tutor intervals
    tutor_iter = iter(intervals['tutor'])
    tutor_tuples = zip(tutor_iter, tutor_iter)
    tutor_intervals = [Interval(tup) for tup in tutor_tuples]
    for lesson_second in lesson_interval.range():
        pupil_is_active = any(lesson_second in pupil_interval.range() for pupil_interval in pupil_intervals)
        tutor_is_active = any(lesson_second in tutor_interval.range() for tutor_interval in tutor_intervals)
        if pupil_is_active and tutor_is_active and lesson_second not in seconds:
            seconds.append(lesson_second)
    return len(seconds)
