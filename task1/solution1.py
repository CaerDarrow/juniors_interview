def strict(func):
	def check(*args, **kwargs):
		types = func.__annotations__
		for arg in (args):
			if not isinstance(arg, types['return']):
				raise TypeError
		return func(*args, **kwargs)
	return check


@strict
def sum_two(a: int, b: int) -> int:
	return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError