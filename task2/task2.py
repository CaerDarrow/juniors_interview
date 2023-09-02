import requests
from bs4 import BeautifulSoup
from collections import Counter
import csv

PARCER_PARAMS = {
    'domain_url': 'https://ru.wikipedia.org/',
    'start_url': 'https://ru.wikipedia.org/w/index.php?title='
                 '%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%'
                 'D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82'
                 '%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB'
                 '%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D'
                 '0%90',
    'last_url': 'https://ru.wikipedia.org/w/index.php?title=%D'
                '0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B'
                '8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%'
                'D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0'
                '%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%AE&sub'
                'catfrom=%D0%AE&pageuntil=Acalolepta+holotephra'
                '#mw-pages',
}


class WikiCategoryParser:
    def __init__(self, parcer_params: dict) -> None:
        self.domain_url = parcer_params['domain_url']
        self.start_url = parcer_params['start_url']
        self.last_url = parcer_params['last_url']
        self.soup: BeautifulSoup = None
        self.amount_subcategory_by_alpha = {chr(i): 0 for i in
                                            range(ord('А'), ord('Я') + 1)}
        self._flag_exit_parsing: bool = None

    def parse_pages(self):
        """Основная функция, которая парсит страницы от start_url до last_url"""
        print('Начало парсинга!')
        current_url = self.start_url
        self._flag_exit_parsing = False
        while True:
            print(current_url)
            page = requests.get(current_url)
            if page.status_code != 200:
                raise AssertionError('Страница не загрузилась!')
            self.soup = BeautifulSoup(page.content, features='html.parser')
            panel = self._get_nessesary_panel()
            subcategories = self._get_subcategories(panel)
            self._update_amount_subcategory_by_alpha(subcategories)
            if self._flag_exit_parsing:
                break
            current_url = self._get_next_url(panel)
        print('Парсинг окончен!')

    def _get_nessesary_panel(self):
        """Этот метод нужно переопределить, если текущая реализация не подходит
        под другие страницы
        Метод возвращает панель странциы с необходимыми нам данными.
        """
        return self.soup.find(name='div', attrs={'id': 'mw-pages'})

    def _get_next_url(self, panel) -> str:
        """Этот метод нужно переопределить, если текущая реализация не подходит
        под другие страницы
        Метод возвращает ссылку на следующую страницу для парсинга.
        """
        part_url = panel.find_all(name='a', attrs={
            'title': 'Категория:Животные по алфавиту'}, href=True)[1]['href']
        return self.domain_url + part_url

    def _get_subcategories(self, panel) -> list[str]:
        """Этот метод нужно переопределить, если текущая реализация не подходит
        под другие страницы
        Метод возвращает список необходимых подкатегорий.
        """
        sub_panel = panel.find(name='div', attrs={
            'mw-category mw-category-columns'
        })
        res = map(lambda x: x.text, sub_panel.find_all(name='a'))
        return list(res)

    def _get_alpha_cnt_dict(self, subcategories):
        """Метод возвразает кол-во животных по буквам
        и заменяет букву Ё на Е"""

        alpha_cnt_dict = Counter([sub[0] for sub in subcategories])
        if 'Ё' in alpha_cnt_dict.keys():
            if 'Е' in alpha_cnt_dict.keys():
                alpha_cnt_dict['Е'] += alpha_cnt_dict['Ё']
            else:
                alpha_cnt_dict['Е'] = alpha_cnt_dict['Ё']
            del alpha_cnt_dict['Ё']
        return alpha_cnt_dict

    def _update_amount_subcategory_by_alpha(self,
                                            subcategories: list[str]) -> None:
        """Метод обновляет словарь с кол-вом живодных по буквам"""

        alpha_cnt_dict = self._get_alpha_cnt_dict(subcategories)

        for key, val in alpha_cnt_dict.items():
            try:
                self.amount_subcategory_by_alpha[key] += val
                print(f'Словарь обновлен. '
                      f'{key}: +{val}')
            except KeyError as e:
                self._flag_exit_parsing = True

    def save_into_csv(self, file_name):
        """Сохраняет amount_subcategory_by_alpha в csv-файл"""
        print(f'Запись результата в файл: {file_name}')
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for row in self.amount_subcategory_by_alpha.items():
                writer.writerow(row)
        print('Запись окончена!')


if __name__ == '__main__':
    # start_url = 'https://ru.wikipedia.org//w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%90&pagefrom=%D0%AF%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BC%D1%83%D1%85%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0&subcatfrom=%D0%90#mw-pages'
    # last_url = 'https://ru.wikipedia.org//w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%90&pagefrom=%D0%AF%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BC%D1%83%D1%85%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0&subcatfrom=%D0%90#mw-pages'

    wiki_parcer = WikiCategoryParser(PARCER_PARAMS)
    wiki_parcer.parse_pages()
    wiki_parcer.save_into_csv('beasts.csv')
    wiki_parcer.save_into_csv('test_beasts.csv')
