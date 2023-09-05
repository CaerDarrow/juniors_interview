from typing import Callable, Any

import pytest

from task1 import strict


@pytest.fixture(scope="session")
def functions_test_1() -> list[Callable]:
	"""
	:return: functions set for task1 funtion testing
	"""
	@strict
	def sum_(x: float, y: float) -> float:
		return x + y

	@strict
	def concat(s_1: str, s_2: str, s_3: str) -> str:
		return s_1 + s_2 + s_3

	@strict
	def add_bool(a: bool, b: bool) -> int:
		return a + b

	@strict
	def args_to_list(a: int, b: float, c: str, d: bool) -> list[Any]:
		return [a, b, c, d]

	return [sum_, concat, add_bool, args_to_list]
