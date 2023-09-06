import unittest
import subprocess

from config import FILENAME, TEST_FILENAME
from solution import main


class WikiTestCase(unittest.TestCase):
    """Тесты результатов парсинга Википедии"""

    def setUp(self) -> None:
        self.csv = open(TEST_FILENAME, 'r')

    def test_parse(self):
        main()
        with open(FILENAME, 'r') as file:
            self.assertListEqual(
                list(self.csv),
                list(file),
                'Вероятно, список животных пополнился'
            )

    def tearDown(self) -> None:
        self.csv.close()


if __name__ == '__main__':
    subprocess.run('playwright install')
    unittest.main()
