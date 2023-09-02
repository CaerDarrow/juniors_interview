import unittest
from solution import parser


class TestCase(unittest.TestCase):

    def test_valid_url(self):
        result = parser(url="https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")
        self.assertEqual(result, 0)

    def test_invalid_url(self):
        result = parser(url="https://ru.wikipedia.orgi/wiki")
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
