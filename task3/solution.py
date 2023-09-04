def get_list(inter: list) -> list:
    temp_list = []
    for item in range(0, len(inter), 2):
        temp_list.append((inter[item], inter[item + 1]))
    return temp_list


def appearance(intervals: dict[str, list[int]]) -> int:
    pupil_time = get_list(intervals['pupil'])
    tutor_time = get_list(intervals['tutor'])
    start_lesson = intervals['lesson'][0]
    end_lesson = intervals['lesson'][1]

    cross_time = []
    summary_time = 0
    for pupil_item in pupil_time:
        for tutor_item in tutor_time:
            start1 = pupil_item[0]
            end1 = pupil_item[1]
            start2 = tutor_item[0]
            end2 = tutor_item[1]

            if end1 > start2 and end2 > start1:
                cross_time = [max(start1, start2, start_lesson), min(end1, end2, end_lesson)]
                summary_time += cross_time[1] - cross_time[0]

    return summary_time


ad = {'intervals': {'lesson': [1594692000, 1594695600],
                    'pupil': [1594692033, 1594696347],
                    'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
      'answer': 3565
      }

if __name__ == '__main__':
    print(appearance(ad['intervals']))
