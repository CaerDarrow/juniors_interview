from juniors_interview.task3.solution import appearance


class TestAppearance:
    def test_one(self):
        data = {'intervals': {'lesson': [1594663200, 1594666800],
                              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
                'answer': 3117
                }
        assert appearance(data['intervals']) == data['answer']

    def test_two(self):
        data = {'intervals': {'lesson': [1594692000, 1594695600],
                              'pupil': [1594692033, 1594696347],
                              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
                'answer': 3565
                }
        assert appearance(data['intervals']) == data['answer']

    def test_three(self):
        data = {'intervals': {'lesson': [1594694000, 1594696700],
                              'pupil': [1594694000, 1594696700],
                              'tutor': [1594694000, 1594696700]},
                'answer': 2700
                }
        assert appearance(data['intervals']) == data['answer']
