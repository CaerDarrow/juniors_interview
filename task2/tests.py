import re
import unittest

from solution import alphabet


class TestFile(unittest.TestCase):

    def test_rows(self):
        count = 0
        with open('animals.csv', 'r', encoding='utf-8') as file:
            for _ in file:
                count += 1
        return self.assertEqual(count, len(alphabet))

    def test_format(self):
        with open('animals.csv', 'r', encoding='utf-8') as file:
            for line in file:
                with self.subTest(line=line):
                    self.assertIsNotNone(re.match(r'(\w+),(\d+)', line))
