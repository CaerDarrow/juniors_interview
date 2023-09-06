import unittest
from .solution import strict, sum_two  # декоратор и декорируемая функция


class TestDecorator(unittest.TestCase):
    # проверка некорректную работу
    def test_correct_sum_two(self):
        res = sum_two(21, 33)  # отсылаем данные для проверки и ожидаем ответ - 54
        self.assertEqual(res, 54)  # проверка на правильность результата

    # проверка на некорректную работу с float
    def test_sum_two_incorrect(self):
        self.assertRaises(TypeError, sum_two, (13, 12.16))  # проверка, что вызывается исключение TypeError

    # проверка на некорректную работу с bool
    def test_sum_two_incorrect_bool(self):
        self.assertRaises(TypeError, sum_two, (1, True))  # проверка, что вызывается исключение TypeError

    # проверка на некорректную работу с str
    def test_sum_two_incorrect_(self):
        self.assertRaises(TypeError, sum_two, (12, 'str'))  # проверка, что вызывается исключение TypeError


if __name__ == '__main__':
    unittest.main()
