"""
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии
список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту)
и записывать в файл в формате `beasts.csv` количество животных на каждую
букву алфавита. Содержимое результирующего файла:
csv
А,642
Б,412
В,....
Примечание:
анализ текста производить не нужно, считается любая запись из категории
(в ней может быть не только название, но и, например, род)
"""

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup, element

START_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

alph_dict = {}


def get_soup(url: str, session: requests.Session) -> BeautifulSoup:
    """Получаем суп из сессии"""
    content = session.get(url).content
    return BeautifulSoup(content, 'lxml')


def get_next_link(url: str, session: requests.Session) -> element.Tag:
    """Ищем на странице ссылку на следующую страницу"""
    soup = get_soup(url, session)
    return soup.find('a', string='Следующая страница')


def parse_func(url: str, session: requests.Session) -> None:
    """Парсим страницу"""
    soup = get_soup(url, session)
    print(f'Parsing: {url}')
    allpages = soup.findAll(
        name='div',
        attrs={'class': 'mw-category mw-category-columns'})
    for data in allpages:
        links = data.findAll('a')
        for i in links:
            if i.get_text()[0] in alph_dict:
                alph_dict[i.get_text()[0]] += 1
            else:
                alph_dict[i.get_text()[0]] = 1


def get_dict_counts(base_url: str) -> dict:
    """Получаем стартовую страницу для парсинга, потом в цикле получаем
    следующую"""
    with requests.Session() as session:
        parse_func(START_URL, session)
        next_link = get_next_link(START_URL, session)
        while next_link is not None:
            url = urljoin(base_url, next_link['href'])
            parse_func(url, session)
            next_link = get_next_link(url, session)
    return alph_dict


def write_file() -> None:
    """Записываем словарь в файл"""
    my_dict = get_dict_counts(START_URL)
    with open(file='beasts.csv',
              mode='w',
              encoding='UTF-8') as file:
        for key, value in my_dict.items():
            file.write(f'{key},{value}\n')


if __name__ == '__main__':
    write_file()
