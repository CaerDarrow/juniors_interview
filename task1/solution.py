import inspect

def strict(func):
    def wrapper(*args, **kwargs):
        parameter_types = inspect.signature(func).parameters  # Get the parameter types from the function signature
        for arg, param_type in zip(args, parameter_types.values()):
            if not isinstance(arg, param_type.annotation):
                raise TypeError(f"Argument '{arg}' is not of type '{param_type.annotation.__name__}'")
        return func(*args, **kwargs)
    return wrapper


def test_strict_decorator():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    # Test case 1: Arguments of correct types
    result = sum_two(1, 2)
    assert result == 3, f"Expected: 3, Actual: {result}"

    # Test case 2: Arguments of incorrect types
    try:
        sum_two(1, 2.4)
    except TypeError:
        pass  # Expected TypeError, so the test passes
    else:
        assert False, "Expected TypeError, but no exception was raised"

    # Test case 3: Arguments with incorrect number of arguments
    try:
        sum_two(1)
    except TypeError:
        pass  # Expected TypeError, so the test passes
    else:
        assert False, "Expected TypeError, but no exception was raised"

    # Test case 4: Arguments with incorrect number of keyword arguments
    try:
        sum_two(a=1, b=2, c=3)
    except TypeError:
        pass  # Expected TypeError, so the test passes
    else:
        assert False, "Expected TypeError, but no exception was raised"

    print("All test cases passed.")

test_strict_decorator()