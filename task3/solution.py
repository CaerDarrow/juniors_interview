def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = range(intervals["lesson"][0], intervals["lesson"][1])
    tutor = map(lambda x: range(*x), zip(intervals["tutor"][::2], intervals["tutor"][1::2]))
    pupil = map(lambda x: range(*x), zip(intervals["pupil"][::2], intervals["pupil"][1::2]))
    return len(set(lesson) & set().union(*pupil) & set().union(*tutor))
