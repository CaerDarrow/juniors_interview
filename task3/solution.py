def correct_interval(interval: list[int]) -> list[int]:
    doublets = []
    for i in range(0, len(interval), 2):
        doublets.append((interval[i], interval[i + 1]))
    doublets.sort(key=lambda x: x[0])
    correct = [doublets[0][0], doublets[0][1]]

    if len(doublets) > 1:
        for i in range(1, len(doublets)):
            left, right = doublets[i]
            j = 1
            while j <= len(correct) - 1:
                if left <= correct[j] < right:
                    correct[j] = right
                    break
                if left <= correct[j] and right <= correct[j]:
                    break
                else:
                    j += 2
            else:
                correct += [left, right]

    return correct


def appearance(intervals: dict[str, list[int]]) -> int:
    start, end = intervals.get('lesson')
    pupil = correct_interval(intervals.get('pupil'))
    tutor = correct_interval(intervals.get('tutor'))
    total = 0
    i, j = 0, 0
    while i < len(tutor) - 1 and j < len(pupil) - 1:
        pupil_start, pupil_end = pupil[j], pupil[j + 1]
        tutor_start, tutor_end = tutor[i], tutor[i + 1]
        left = max(pupil_start, tutor_start)
        right = min(pupil_end, tutor_end)
        if right > left:
            sub_interval = [max(pupil_start, tutor_start), min(pupil_end, tutor_end)]
            if sub_interval[0] < start < sub_interval[1]:
                sub_interval[0] = start
            if sub_interval[0] < end < sub_interval[1]:
                sub_interval[1] = end
            if sub_interval[0] >= start and sub_interval[1] <= end:
                total += sub_interval[1] - sub_interval[0]
        if pupil_end < tutor_end:
            j += 2
        else:
            i += 2
    return total
