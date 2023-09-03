from solution import trunc_times, intersection_times, unioun_times

test_trunc_data = [
    (([1, 2, 3, 4, 5, 6], 2, 4), [3, 4]),
    (([1, 2, 3, 4, 5, 6], 0, 7), [1, 2, 3, 4, 5, 6]),
    (([1, 3, 5, 7, 9, 11], 2, 10), [2, 3, 5, 7, 9, 10]),
    (([1, 3, 5, 7, 9, 11], 2, 11), [2, 3, 5, 7, 9, 11]),
    (([1, 3, 5, 7, 9, 11], 1, 10), [1, 3, 5, 7, 9, 10])
]

test_intersection_data = [
    ([1, 3, 5, 7], [2, 4, 6, 8], 2),
    ([1, 9], [2, 4, 6, 8], 4),
    ([2, 4, 6, 8], [1, 9], 4),
    ([1, 7, 12, 16], [1, 4, 7, 9], 3)
]

test_union_data = [
    ([1, 3, 2, 4], [1, 4]),
    ([1, 3, 2, 4, 5, 7], [1, 4, 5, 7]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 2, 3, 7, 6, 8], [1, 2, 3, 8])
]


def test_trunc_times(test_data: tuple[tuple[list, int, int], list[int]]) -> None:
    for i, (input_data, output_data) in enumerate(test_data):
        func_result = trunc_times(*input_data)
        assert func_result == output_data, f'Error on test case {i}, got {func_result}, expected {output_data}'


def test_union_times(test_data: tuple[list, list]) -> None:
    for i, (input_data, output_data) in enumerate(test_data):
        func_result = unioun_times(input_data)
        assert func_result == output_data, f'Error on test case {i}, got {func_result}, expected {output_data}'


def test_intersection_times(test_data: tuple[list, list, int]) -> None:
    for i, (pupil_data, tutor_data, summ) in enumerate(test_data):
        func_result = intersection_times(pupil_data, tutor_data)
        assert func_result == summ, f'Error on test case {i}, got {func_result}, expected {summ}'


if __name__ == '__main__':
    test_trunc_times(test_trunc_data)
    test_union_times(test_union_data)
    test_intersection_times(test_intersection_data)
