from unittest import TestCase
from bs4 import BeautifulSoup
import os

from task2.solution import get_html, get_next_page, parser, write_to_file, URL_CATEGORY


class TestSolution(TestCase):

    def test_get_html(self):
        html = get_html(URL_CATEGORY)
        self.assertIn("html", html)

    def test_get_next_page(self):
        html = '''
        <a href="/page2" title="Категория:Животные по алфавиту">Следующая страница</a>
        <a href="/page2" title="Категория:Животные по алфавиту">Следующая страница</a>
        '''
        page = BeautifulSoup(html, 'html.parser')
        next_page = get_next_page(page)
        self.assertEqual(next_page, '/page2')

    def test_write_to_file(self):
        data = {'A': 1, 'B': 2}
        write_to_file(data)
        self.assertTrue(os.path.exists('beasts.csv'))


if __name__ == '__main__':
    unittest.main()
