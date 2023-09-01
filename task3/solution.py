from datetime import datetime, timedelta


def filter_timestamps(timestamps):
    timestamps.sort()  # Сортируем временные метки по возрастанию

    filtered_timestamps = []
    current_start = None
    current_end = None

    for start, end in timestamps:
        if current_start is None:
            # Если текущий интервал пуст, устанавливаем начало и конец текущего интервала
            current_start = start
            current_end = end
        else:
            if start <= current_end:
                # Если новый интервал начинается до текущего конца, расширяем текущий интервал
                current_end = max(current_end, end)
            else:
                # Если новый интервал начинается после текущего конца, добавляем текущий интервал в отфильтрованный список
                filtered_timestamps.append([current_start, current_end])
                # Устанавливаем новое начало и конец текущего интервала
                current_start = start
                current_end = end

    # Добавляем последний текущий интервал в отфильтрованный список
    filtered_timestamps.append([current_start, current_end])

    return filtered_timestamps


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]
    pupil_intervals = [
        intervals["pupil"][i : i + 2] for i in range(0, len(intervals["pupil"]), 2)
    ]
    tutor_intervals = [
        intervals["tutor"][i : i + 2] for i in range(0, len(intervals["tutor"]), 2)
    ]

    tutor_presence = []
    pupil_presence = []

    for pupil_interval in pupil_intervals:
        if lesson_start > pupil_interval[0] and lesson_start > pupil_interval[1]:
            continue
        if lesson_end < pupil_interval[0] and lesson_end < pupil_interval[1]:
            continue
        if lesson_start > pupil_interval[0] and lesson_start <= pupil_interval[1]:
            pupil_presence.append([lesson_start, pupil_interval[1]])
            continue
        if lesson_end >= pupil_interval[0] and lesson_end < pupil_interval[1]:
            pupil_presence.append([pupil_interval[0], lesson_end])
            continue
        if lesson_start <= pupil_interval[0] and lesson_end >= pupil_interval[1]:
            pupil_presence.append([pupil_interval[0], pupil_interval[1]])
            continue

    pupil_seconds = timedelta()
    
    if pupil_presence == []:
        return 0
    
    for timestamp in filter_timestamps(pupil_presence):
        pupil_seconds += datetime.fromtimestamp(timestamp[1]) - datetime.fromtimestamp(
            timestamp[0]
        )

    for tutor_interval in tutor_intervals:
        if lesson_start > tutor_interval[0] and lesson_start > tutor_interval[1]:
            continue
        if lesson_end < tutor_interval[0] and lesson_end < tutor_interval[1]:
            continue
        if lesson_start > tutor_interval[0] and lesson_start <= tutor_interval[1]:
            tutor_presence.append([lesson_start, tutor_interval[1]])
            continue
        if lesson_end >= tutor_interval[0] and lesson_end < tutor_interval[1]:
            tutor_presence.append([tutor_interval[0], lesson_end])
            continue
        if lesson_start <= tutor_interval[0] and lesson_end >= tutor_interval[1]:
            tutor_presence.append([tutor_interval[0], tutor_interval[1]])
            continue

    tutor_seconds = timedelta()
    
    if tutor_presence == []:
        return 0
    
    for timestamp in filter_timestamps(tutor_presence):
        tutor_seconds += datetime.fromtimestamp(timestamp[1]) - datetime.fromtimestamp(
            timestamp[0]
        )

    total_lesson_seconds = datetime.fromtimestamp(lesson_end) - datetime.fromtimestamp(
        lesson_start
    )
    print(((pupil_seconds.seconds - 9) + (tutor_seconds.seconds - 9)) / 2)
    print(total_lesson_seconds)

    return int((pupil_seconds.seconds + tutor_seconds.seconds) / 2)


import unittest


class TestAppearance(unittest.TestCase):
    def test_appearance(self):
        intervals = {
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
        }
        self.assertEqual(appearance(intervals), 3150)

        intervals = {
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
        }
        self.assertEqual(appearance(intervals), 3588)

        intervals = {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        }
        self.assertEqual(appearance(intervals), 3574)

        # Test case with no overlap
        intervals = {
            "lesson": [1594702800, 1594706400],
            "pupil": [1594702789, 1594702790, 1594706401, 1594706402],
            "tutor": [1594700000, 1594702790, 1594706401, 1594709200],
        }
        self.assertEqual(appearance(intervals), 0)

        # Test case with one interval completely within another
        intervals = {
            "lesson": [1594702800, 1594706400],
            "pupil": [1594702900, 1594705000],
            "tutor": [1594702500, 1594707000],
        }
        self.assertEqual(appearance(intervals), 3150)


if __name__ == "__main__":
    unittest.main()
