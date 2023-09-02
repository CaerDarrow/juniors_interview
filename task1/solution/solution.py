def strict(func):
    def wrapper(*args, **kwargs):
        expected_annotations = func.__annotations__

        # check positional args
        got_annotations = [type(x) for x in args]
        arg_num = 1
        for first, second in zip([v for k, v in expected_annotations.items()], got_annotations):
            if first != second:
                raise TypeError(f"Expected {first}, got {second} in arg №{arg_num}")
            arg_num += 1

        # check kw args
        for k, v in kwargs.items():
            i_type = type(v)
            i_kw = k
            if expected_annotations[i_kw] != i_type:
                raise TypeError(f"Expected arg `{i_kw}` is {expected_annotations[i_kw]} not {i_type}")

        return func(*args, **kwargs)

    return wrapper


"""
Example how to use my decorator

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1.3, 2))  # >>> 3
print(sum_two(a=1, b=2.4))  # >>> TypeError
"""
