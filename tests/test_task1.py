from typing import Callable

import pytest

from tests.utils.task1 import generate_func_kwargs


def test_positive(functions_test_1: list[Callable]):
	for func in functions_test_1:
		func_kwargs = generate_func_kwargs(func, "positive")
		try:
			func(**func_kwargs)
		except TypeError as err:
			raise AssertionError("Unexpected error: " + str(err))


def test_negative(functions_test_1: list[Callable]):
	for func in functions_test_1:
		func_kwargs = generate_func_kwargs(func, "negative")
		with pytest.raises(TypeError):
			func(**func_kwargs)
