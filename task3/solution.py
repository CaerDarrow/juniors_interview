from typing import NamedTuple, Optional


class Interval(NamedTuple):
    start: int
    end: int


def get_intervals(timestamps: list[int]) -> list[Interval]:
    return [Interval(timestamps[i], timestamps[i + 1]) for i in range(0, len(timestamps), 2)]


def get_general(a: Interval, b: Interval) -> Optional[Interval]:
    if b.start < a.start:
        a, b = b, a
        
    if a.end > b.end:
        return b
    
    if b.start < a.end <= b.end:
        return Interval(b.start, a.end)
    
    return None


def limit(interval: Interval, limit: Interval) -> Optional[Interval]:
    start = max(interval.start, limit.start)
    end = min(interval.end, limit.end)
    
    if start >= end:
        return None
    
    return Interval(start, end)
        
        
def merge_intervals_if_overrides(intervals: list[Interval]):
    merged = []
    chain_start = intervals[0].start
    chain_end = intervals[0].end
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        
        if chain_end >= current.start:
            chain_end = max(chain_end, current.end)
            continue
        
        merged.append(Interval(chain_start, chain_end))
        chain_start = current.start
        chain_end = current.end
        
    merged.append(Interval(chain_start, chain_end))
        
    return merged


def appearance(intervals: dict[str, list[int]]) -> int:
    pupil_intervals = get_intervals(intervals['pupil'])
    tutor_intervals = get_intervals(intervals['tutor'])
    lesson_interval = get_intervals(intervals['lesson'])[0]
    
    pupil_intervals.sort(key=lambda i: i.start)
    tutor_intervals.sort(key=lambda i: i.start)
    
    pupil_intervals = merge_intervals_if_overrides(pupil_intervals)
    tutor_intervals = merge_intervals_if_overrides(tutor_intervals)
    
    pupil_index = 0
    tutor_index = 0
    
    res = 0
    
    while pupil_index != len(pupil_intervals) and tutor_index != len(tutor_intervals):
        pupil_interval = pupil_intervals[pupil_index]
        tutor_interval = tutor_intervals[tutor_index]
        
        if  pupil_interval.end <= tutor_interval.start:
            pupil_index += 1
            continue
        
        if tutor_interval.end <= pupil_interval.start:
            tutor_index += 1
            continue
            
        intersection = get_general(pupil_interval, tutor_interval)
        
        if intersection is None:
            continue
        
        intersection = limit(intersection, lesson_interval)
        
        if intersection is None:
            break
            
        res += intersection.end - intersection.start
        
        if pupil_interval.end <= tutor_interval.end:
            pupil_index += 1
        else:
            tutor_index += 1
            
    return res


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

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       aaa  = 0
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    