import pytest
from task1.solution import strict, sum_two

def test_sum_two_correct():
    assert sum_two(1, 2) == 3

def test_sum_two_incorrect_type():
    with pytest.raises(TypeError):
        sum_two(1, "2")

def test_sum_two_incorrect_kwarg():
    with pytest.raises(TypeError):
        sum_two(a=1, b="2")
