"""Подсчет элементов, взятых из википедии и начинающиеся на первую букву."""

import logging
from collections import Counter
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def save_txt(name_file: str, data: dict[str, int]) -> None:
    """Сохранение данные в текстовой файл."""
    with open(name_file, encoding='utf-8', mode='w') as txtfile:
        for key, value in sorted(data.items()):
            txtfile.write(f'{key}, {value}\n')


def save_csv(name_file: str, data: dict[str, int]) -> None:
    """Сохранение данных в csv-файл."""
    import csv
    with open(name_file, encoding='utf-8', mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for elem in sorted(data.items()):
            writer.writerows([elem])

def counter_parsed(link: str) -> dict[str, int]:
    """Парсирование страницы википедии и счет животных на первую букву."""
    parsed_url = urlparse(link)
    base_url = parsed_url.scheme + '://' + parsed_url.netloc
    counter = Counter()
    while link:
        url = urljoin(base_url, link)
        page = requests.get(url)
        if page.status_code != requests.codes.ok:
            raise requests.exceptions.HTTPError('Ошибка')
        logger.debug(f'{"-"*120}\nОбрабатывает {unquote(url)}')

        soup = BeautifulSoup(page.text, 'html.parser')
        main_block = soup.find(id='mw-pages')

        groups = main_block.find_all(class_='mw-category-group')
        for group in groups:
            elements = group.find_all('a')
            letter = elements[0].text.strip()[0]
            counter[letter] += len(elements)
            logger.debug(f'{letter}, {len(elements)}')

        link = main_block.find('a', string='Следующая страница')
        if link:
            link = link.get('href')
    return counter


def main():
    logger.debug('Старт программы')

    NAME_FILE_CSV = 'beasts.csv'
    link = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    counter = counter_parsed(link)

    save_csv(NAME_FILE_CSV, counter)
    logger.debug('Завершение программы')


if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    main()
