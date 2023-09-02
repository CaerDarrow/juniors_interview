import unittest
import csv
import os 

from solution import pars_data, write_to_csv


class TestFunctions(unittest.TestCase):
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    data = pars_data(url)

    def tearDown(self):
        # Выполняется после каждого теста
        if os.path.exists("test.csv"):
            os.remove("test.csv")

    def test_pars_data(self):
        self.assertIsInstance(self.data, dict)
        self.assertTrue(len(self.data) != 0)
        for key in self.data.keys():
            self.assertFalse(key.isascii())

    def test_write_to_csv(self):
        write_to_csv('test.csv', self.data)
        with open('test.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for key, value in self.data.items():
            self.assertIn([key, str(value)], rows)


if __name__ == '__main__':
    unittest.main()
