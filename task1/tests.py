import pytest
from solution import strict


class TestStrict:
    """Тестирование функции strict"""

    @staticmethod
    @strict
    def int_func(i: int, j: int):
        return True

    @staticmethod
    @strict
    def float_func(i: float, j: float):
        return True

    @staticmethod
    @strict
    def int_float_func(i: int, j: float):
        return True

    @pytest.mark.parametrize(
        "func, arg1, arg2", [
            (int_func, 1, 1),
            (float_func, 2.0, 2.2),
            (int_float_func, 3, 3.2),
        ]
    )
    def test_common_work(self, func, arg1, arg2):
        """Проверка на работу при заданных позиционных аргументах"""
        assert func(arg1, arg2)

    @pytest.mark.parametrize(
        "func, kwargs", [
            (int_func, {'i': 10, 'j': 20}),
            (float_func, {'i': 10.1, 'j': 20.2}),
            (int_float_func, {'i': 30, 'j': 30.3}),
        ]
    )
    def test_work_with_kwargs(self, func, kwargs):
        """Проверка на работу при заданных именованных аргументах"""
        assert func(**kwargs)

    @pytest.mark.parametrize(
        "func, arg, kwargs", [
            (int_func, 10, {'j': 20}),
            (float_func, 20.1, {'j': 20.2}),
            (int_float_func, 31, {'j': 30.3}),
        ]
    )
    def test_work_with_mix_args(self, func, arg, kwargs):
        """Проверка на работу при заданных именованных
        и позиционных аргументах"""
        assert func(arg, **kwargs)

    @staticmethod
    @strict
    def bool_none_func(flag: bool, without_type):
        return True

    def test_error_1(self):
        """Проверка вызова ошибки, при неуказанных типах."""
        with pytest.raises(AssertionError, match=r'^Не у всех'):
            assert self.bool_none_func(True, 1)

    @pytest.mark.parametrize(
        "func, arg1, arg2", [
            (int_func, 'hello', 1),
            (float_func, 2.0, 2),
            (int_float_func, 1.0, True),
        ]
    )
    def test_error_2(self, func, arg1, arg2):
        with pytest.raises(TypeError, match=r'^Значение'):
            assert func(arg1, arg2)
