from typing import Callable, Any


def strict(foo: Callable) -> Callable:
	def wrapper(*args, **kwargs) -> Any:
		typing_ = foo.__annotations__
		if args:
			for arg in args:
				arg_name = list(typing_)[args.index(arg)]
				kwargs[arg_name] = arg
		if any(
			(not isinstance(kwargs[arg_], typing_[arg_]) for arg_ in kwargs)
		):
			raise TypeError
		return foo(**kwargs)
	wrapper.__wrapped__ = foo  # for auto testing
	return wrapper
