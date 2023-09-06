from solution import strict



@strict
def add_strings(a: str, b: str):
    return a + b


@strict
def multiply_numbers(a: int, b: int):
    return a * b


def test_add_strings():
    try:
        result = add_strings('Hello', 'World')
        assert result == 'HelloWorld', "Test failed: Addition of two strings"
    except TypeError:
        raise AssertionError("Test failed: Unexpected TypeError for matching argument types")


def test_multiply_numbers():
    try:
        result = multiply_numbers(30, 10)
        assert result == 300, 'Test failed: Multiplication of two integers'
    except TypeError:
        raise AssertionError("Test failed: Unexpected TypeError for matching argument types")


def test_mismatched_arguments():
    try:
        add_strings(5, "10")
    except TypeError:
        pass
    else:
        raise AssertionError("Test failed: Expected TypeError for mismatched argument types")


if __name__ == "__main__":
    test_add_strings()
    test_multiply_numbers()
    test_mismatched_arguments()

print("All tests passed!")

