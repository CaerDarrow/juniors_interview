import unittest


def strict(func):
    """Checks if passed parameters types are correct."""
    def wrapper(*args, **kwargs):
        # Create a list of tuples (param_name, param_type)
        annotations = list(func.__annotations__.items())
        i = 0

        for arg in args:
            check_type(arg, annotations[i])
            i += 1

        for kwarg_value in kwargs.values():
            check_type(kwarg_value, annotations[i])
            i += 1

        return func(*args, **kwargs)

    def check_type(arg, annotation):
        """Raises a TypeError if parameter type doesn't match a correct type."""
        correct_type = annotation[1]
        if not isinstance(arg, correct_type):
            raise TypeError(f'Function {func.__name__} parameter\'s {annotation[0]} '
                            f'type is {type(arg)} instead of {correct_type}.')

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def test_different_types(a: int, b: float, c: str, d: bool) -> dict:
    result = {'sum': a + b, c: d}
    return result


class StrictTests(unittest.TestCase):
    def test_valid_args(self):
        result = sum_two(1, 2)
        self.assertEqual(result, 3)

        result = test_different_types(1, 1.2, 'Jupiter is a planet', True)
        self.assertEqual(result['sum'], 2.2)
        self.assertTrue(result['Jupiter is a planet'])

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            sum_two(True, '2')

        with self.assertRaises(TypeError):
            test_different_types(4, 1.2, False, 'Some str')


if __name__ == '__main__':
    unittest.main()
