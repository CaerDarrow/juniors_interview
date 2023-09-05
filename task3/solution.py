"""
Эту задачу решить не удалось. Но я пытался. Ход мыслей в любом случае правильный - сравнивать range'ы
 (совпадение временных отрезков). Другого варианта, по крайней мере, не представляю.
Пробовал по-разному - не совпадают ответы с тестовыми.
И по сложности - при таком алгоритме получается в общем случае O(n * m). Как сделать проще - не смог понять.
"""


def appearance(intervals: dict[str, list[int]]) -> int:
	pupil, tutor, lesson = intervals["pupil"], intervals["tutor"], intervals["lesson"]
	lesson_start, lesson_end = lesson[0], lesson[1]

	if any(
		(len(lst) % 2 != 0 for lst in (pupil, tutor, lesson))
	):
		raise ValueError("Expected for even list numbers amount")

	def clean_up_intervals_by_lesson(lst: list[int]) -> list[int]:
		idx = 0
		for _ in range(len(lst) // 2):
			start_ts, end_ts = lst[idx], lst[idx + 1]
			if start_ts < lesson_start:
				if end_ts > lesson_start:
					lst[idx] = lesson_start
				else:
					del lst[idx]
					del lst[idx + 1]
					continue
			elif start_ts > lesson_start:
				if end_ts > lesson_end:
					lst[idx + 1] = lesson_end
			idx += 2
		return lst

	pupil, tutor = clean_up_intervals_by_lesson(pupil), clean_up_intervals_by_lesson(tutor)

	idx = 0
	sum_ = 0
	for _ in range(len(pupil) // 2):
		start_ts, end_ts = pupil[idx], pupil[idx + 1]
		idx_ = 0
		for __ in range(len(tutor) // 2):
			start_ts_tutor, end_ts_tutor = tutor[idx_], tutor[idx_ + 1]
			rng = range(start_ts_tutor, end_ts_tutor + 1)
			if start_ts in rng:
				if end_ts in rng:
					sum_ += (end_ts - start_ts)
				else:
					sum_ += (end_ts_tutor - start_ts)
			else:
				if start_ts < start_ts_tutor:
					if end_ts in rng:
						sum_ += (end_ts - start_ts_tutor)
					elif end_ts > end_ts_tutor:
						sum_ += (end_ts_tutor - start_ts_tutor)
		idx += 2

	return sum_


tests = [
	{'intervals': {'lesson': [1594663200, 1594666800],
				   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
				   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
	 'answer': 3117
	 },
	{'intervals': {'lesson': [1594702800, 1594706400],
				   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
							 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
							 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
							 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
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
		assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
