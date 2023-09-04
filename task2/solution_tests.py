import os
import unittest

from solution import parse_animals_count


class TestAnimalParser(unittest.TestCase):

    def test_parse_animals_count(self):
        test_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

        parse_animals_count(test_url)

        # Проверяем наличие созданного файла beasts.csv
        self.assertTrue(os.path.exists('beasts.csv'))

        # Проверяем, что файл beasts.csv не пустой
        with open('beasts.csv', 'r', encoding='UTF-8') as b:
            file_contents = b.read()
            self.assertTrue(len(file_contents) > 0)

        with open('beasts.csv', 'r', encoding='UTF-8') as b:
            lines = b.readlines()
            counts = {}
            for line in lines:
                letter, count = line.strip().split(', ')
                counts[letter] = int(count)

            # Проверка для буквы 'А'
            self.assertTrue('А' in counts)
            self.assertEqual(counts['А'], 1226)


if __name__ == '__main__':
    unittest.main()
