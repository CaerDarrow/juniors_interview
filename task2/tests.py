import unittest
import wikipediaapi
import os
from solution import get_categorymembers
from solution import write_csv


class TestGetCategoryMembers(unittest.TestCase):
    def setUp(self):
        self.wiki_wiki = wikipediaapi.Wikipedia('juniors-tets (rh26157@gmail.com)', 'ru')
        self.cat = self.wiki_wiki.page("Категория:Животные по алфавиту")

    def test_get_categorymembers(self):
        data = get_categorymembers(self.cat.categorymembers)
        self.assertTrue(isinstance(data, dict))
        self.assertGreater(len(data), 0)


class TestWriteCSV(unittest.TestCase):
    def setUp(self):
        self.data = {'A': 5, 'B': 10, 'C': 15}
        self.filename = 'beasts.csv'

    def test_write_csv(self):
        write_csv(self.data)
        self.assertTrue(os.path.exists(self.filename))
        
        with open(self.filename, 'r', encoding="utf-8") as csvfile:
            lines = csvfile.readlines()
            self.assertEqual(len(lines), len(self.data))
            
            for line in lines:
                parts = line.strip().split(',')
                self.assertEqual(len(parts), 2)
                key, value = parts
                self.assertTrue(key in self.data)
                self.assertEqual(int(value), self.data[key])

    def tearDown(self):
        os.remove(self.filename)


if __name__ == '__main__':
    unittest.main()
