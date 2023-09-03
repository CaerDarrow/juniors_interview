def appearance(intervals: dict[str, list[int]]) -> int:
    # get intervals from dict
    lesson_times, pupil_times, tutor_times = (
        intervals["lesson"],
        intervals["pupil"],
        intervals["tutor"],
    )

    # fill start-stop lists
    lesson_start, lesson_end = lesson_times
    pupil_start_times, pupil_end_times = pupil_times[::2], pupil_times[1::2]
    tutor_start_times, tutor_end_times = tutor_times[::2], tutor_times[1::2]

    total_times = (
        set()
    )  # for removing intersections, how to make it more memory-friendly have no good ideas

    for pupil_start, pupil_end in zip(pupil_start_times, pupil_end_times):
        # check is pupil timeinterval into lesson timeinterval
        if pupil_start <= lesson_end and pupil_end >= lesson_start:
            for tutor_start, tutor_end in zip(tutor_start_times, tutor_end_times):
                # check is tutor timeinterval into lesson timeinterval
                if tutor_start <= lesson_end and tutor_end >= lesson_start:
                    if tutor_start <= pupil_end and tutor_end >= pupil_start:
                        # get minimum from stops
                        end = min(pupil_end, tutor_end, lesson_end)
                        # get maximum from starts
                        start = max(pupil_start, tutor_start, lesson_start)
                        # NOTE: min stop and max start means lesson,tutor and pupil 100% was together in one timedelta

                        # fill range into set, grant us have no intersections, we will calc
                        total_times.update(range(start, end))
    return len(total_times)


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print("all test passed")
