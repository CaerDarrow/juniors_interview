from solution import appearance


def test_without_intersections():
    intervals = {
        "intervals": {"lesson": [1, 10], "pupil": [1, 3, 5, 7], "tutor": [1, 8]},
        "answer": 4,
    }

    assert appearance(intervals["intervals"]) == intervals["answer"]


def test_with_intersections():
    intervals = {
        "intervals": {
            "lesson": [1, 10],
            "pupil": [1, 5, 2, 3, 6, 8, 6, 7],
            "tutor": [1, 5, 7, 9],
        },
        "answer": 5,
    }
    assert appearance(intervals["intervals"]) == intervals["answer"]


def test_nobody_came_to_meeting():
    intervals = {
        "intervals": {"lesson": [1, 10], "pupil": [], "tutor": []},
        "answer": 0,
    }
    assert appearance(intervals["intervals"]) == intervals["answer"]
