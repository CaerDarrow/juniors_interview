from solution import appearance


def test_appearance():
    intervals = {
        'lesson': [1594600000, 1594610000],
        'pupil': [1594601000, 1594612000, 1594613000, 1594614000],
        'tutor': [1594602000, 1594603000, 1594605000, 1594608000]
    }
    expected_result = 2400

    result = appearance(intervals)

    assert result == expected_result, f"Test failed. Expected {expected_result}, but got {result}"


test_appearance()
