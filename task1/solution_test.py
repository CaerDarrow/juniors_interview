import pytest
from juniors_interview.task1.solution import strict


class TestStrict:
    def test_one(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        assert sum_two(1, 2) == 3

    def test_two(self):
        @strict
        def sum_two(a: float, b: int) -> float:
            return a + b
        assert sum_two(2.5, 1) == 3.5

    def test_three(self):
        @strict
        def sum_two(a: float, b: float) -> int:
            return a + b
        with pytest.raises(TypeError) as exc:
            sum_two(1.2, 2.2)
        assert str(exc.value) == "Функция вернула неверный тип данных"

    def test_four(self):
        @strict
        def sum_two(a: float, b: int) -> float:
            return a + b
        with pytest.raises(TypeError) as exc:
            sum_two(1, 2)
        assert str(exc.value) == "Аргумент 1 должен быть типа float"
