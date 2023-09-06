import os
import csv
import unittest
from solution import *

class TestWikiParser(unittest.TestCase):

    def test_file_creation(self):
        # проверяем, что файл beasts.csv создается после парсинга
        wiki_parse(URL_BEASTS)
        self.assertTrue(os.path.exists('beasts.csv'))

    def test_csv_format(self):
        # проверяем, что файл beasts.csv содержит данные в правильном формате
        wiki_parse(URL_BEASTS)
        with open('beasts.csv', 'r', encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.assertEqual(len(row), 2)
                self.assertTrue(row[0].isalpha())
                self.assertTrue(row[1].isdigit())

    def test_file_extension(self):
        # проверяем, что файл beasts.csv формата = .csv
        file_name = 'beasts.csv'
        file_extension = os.path.splitext(file_name)[1]
        self.assertEqual(file_extension, '.csv')


if __name__ == '__main__':
    unittest.main()
