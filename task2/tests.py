import pytest
from solution import WikiCategoryParser, PARCER_PARAMS
import csv


class TestWikiParcer:
    """Проверка класса WikiCategoryParser"""
    def test_result(self):
        """Проверка конечного файла на значения"""
        wiki_parcer = WikiCategoryParser(PARCER_PARAMS)
        wiki_parcer.parse_pages()
        result_file_name = 'test_beasts.csv'
        wiki_parcer.save_into_csv(result_file_name)
        check_di = {}
        with open(result_file_name) as file:
            reader = csv.reader(file, delimiter=',')
            for key, val in reader:
                check_di[key] = int(val)

        assert check_di['Э'] == 223
        assert check_di['Ю'] == 138
        assert check_di['Я'] == 213
        assert check_di['А'] == 1226
        assert check_di['Б'] == 1686
