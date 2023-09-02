import pytest
from task3 import appearance


@pytest.mark.parametrize(
    'intervals, expected', [
        ({'intervals': {'lesson': [0, 3000],
                        'pupil': [0, 3000],
                        'tutor': [0, 3000]}},
         3000),
        ({'intervals': {'lesson': [1000, 4000],
                        'pupil': [0, 5000],
                        'tutor': [0, 5000]}},
         4000 - 1000),
        ({'intervals': {'lesson': [1000, 4000],
                        'pupil': [900, 1100, 3000, 3500, 3900, 4000],
                        'tutor': [0, 5000]}},
         700),
        ({'intervals': {'lesson': [1000, 4000],
                        'pupil': [900, 1100, 3000, 3500, 3900, 4000],
                        'tutor': [900, 1100, 3000, 3500, 3900, 4000]}},
         700),
        ({'intervals': {'lesson': [1000, 4000],
                        'pupil': [0,4000],
                        'tutor': [900, 1100, 3000, 3500, 3900, 4000]}},
         700),
        ({'intervals': {'lesson': [1000, 4000],
                        'pupil': [0, 5000],
                        'tutor': [0, 5000]}},
         4000 - 1000),

    ]
)
def test_one(intervals, expected):
    assert appearance(**intervals) == expected
