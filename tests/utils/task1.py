import random
from typing import Callable, Type, Literal

from ..static.task1 import task1_types


def generate_random_arg(type_: type) -> task1_types:
	rand_values = {
		int: random.randrange(100),
		str: random.choice(["some", "words", "set"]),
		float: random.random(),
		bool: random.choice([True, False])
	}
	type_: Type[task1_types]
	return rand_values[type_]


def generate_func_kwargs(
	func: Callable, test_type: Literal["positive", "negative"]
) -> dict[str, task1_types]:
	"""
	:param func: func wrapped by "strict"
	:param test_type: test expectations
	:return: random func args
	"""	
	negative_rand_data = {
		int: bool,
		str: float,
		float: int,
		bool: str
	}

	kwargs = {}
	if hasattr(func, "__wrapped__"):  # чтобы линтер не ругался
		annotations: dict[str, type] = func.__wrapped__.__annotations__
	annotations.pop("return", None)
	for arg_name, arg_type in annotations.items():
		arg_type: Type[task1_types]
		match test_type:
			case "positive":
				rand_value = generate_random_arg(arg_type)
			case "negative":
				rand_value = generate_random_arg(negative_rand_data[arg_type])
		kwargs[arg_name] = rand_value
	return kwargs
