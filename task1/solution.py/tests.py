import pytest
from solution import strict


class TestStrict:

    @staticmethod
    @strict
    def check_int_args(a: int, b: int):
        return True

    @staticmethod
    @strict
    def float_args(a: int, b: int):
        return True

    @staticmethod
    @strict
    def int_float_args(a: int, b: int):
        return True

    @staticmethod
    @strict
    def bool_none_args(flag: bool, without_type):
        return True
    
    @pytest.mark.parametrize(
        "func, arg1, arg2", [
            (check_int_args, 1, 2),
            (float_args, 1.2, 3.4),
            (int_float_args, 1, 2.3),
        ]
    )
    def test_common_func_with_common_types(self, func, arg1, arg2):
        assert func(arg1, arg2)
        

    @pytest.mark.parametrize(
        "func, kwargs", [
            (check_int_args, {'a': 1, 'b': 2}),
            (float_args, {'a': 1.2, 'b': 3.4}),
            (int_float_args, {'a': 1, 'b': 2.3}),
        ]
    )
    def test_func_with_kwargs(self, func, kwargs):
        assert func(**kwargs)

    @pytest.mark.parametrize(
        "func, arg, kwargs", [
            (check_int_args, 1, {'b': 2}),
            (float_args, 1.2, {'b': 3.4}),
            (int_float_args, 1, {'b': 2.3}),
        ]
    )
    def test_func_with_mix_types(self, func, arg, kwargs):
        assert func(arg, **kwargs)

    def test_error_1(self):
        assert self.bool_none_args(True, 1)
