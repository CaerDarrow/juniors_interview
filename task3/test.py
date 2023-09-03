import pytest
from . import solution


def test_appearance():
    tests = [
        {'intervals': {'lesson': [1594663200, 1594666800],
                'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
        'answer': 3117
        },
        {'intervals': {'lesson': [1594702800, 1594706400],
                'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
        'answer': 3577
        },
        {'intervals': {'lesson': [1594692000, 1594695600],
                'pupil': [1594692033, 1594696347],
                'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
        'answer': 3565
        },
    ]
    
    for test in tests:
        assert solution.appearance(test['intervals']) == test['answer']
        
        
I = solution.Interval
        
@pytest.mark.parametrize('intervals, merged', [[[I(11, 1400), I(500, 600), I(2000, 2100)], [I(11, 1400), I(2000, 2100)]],
                                               [[I(1, 5), I(7, 8), I(9, 100)], [I(1, 5), I(7, 8), I(9, 100)]],
                                               [[I(1, 5), I(5, 8), I(9, 100), I(50, 80)], [I(1, 8), I(9, 100)]],])
def test_interval_merging(intervals, merged):
    assert solution.merge_intervals_if_overrides(intervals) == merged
    
    
@pytest.mark.parametrize('interval, limit, correct', [[I(0, 10), I(2, 8), I(2, 8)],
                                                      [I(20, 80), I(10, 90), I(20, 80)],
                                                      [I(20, 80), I(10, 60), I(20, 60)],
                                                      [I(30, 10), I(10, 30), None],
                                                      [I(30, 50), I(50, 30), None]])
def test_limit(interval, limit, correct):
    assert solution.limit(interval, limit) == correct
    
    
@pytest.mark.parametrize('a, b, correct', [[I(1, 50), I(30, 100), I(30, 50)],
                                           [I(100, 200), I(50, 120), I(100, 120)],
                                           [I(1, 10), I(10, 20), None],
                                           [I(1, 5), I(7, 10), None]])
def test_get_general(a, b, correct):
    assert solution.get_general(a, b) == correct
    
    
@pytest.mark.parametrize('timestamps, intervals', [[[1,2,3,4,5,6], [I(1,2), I(3, 4), I(5, 6)]],
                                                   [[1, 20, 10, 30, 3, 5], [I(1, 20), I(10,30), I(3, 5)]],])
def test_get_intervals(timestamps, intervals):
    assert solution.get_intervals(timestamps) == intervals
