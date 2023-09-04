import logging
from collections import Counter

import requests
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def parse_animals_count(url: str) -> None:
    """
    Функция собирает информацию о количестве животных,
    разбитых по алфавиту, с Википедии.

    :param url: Стартовый URL для сбора информации о животных.
    :type url: str

    :return: None
    """
    alphabet_counter = Counter()

    while url:
        request = requests.get(url)
        request_data = request.text

        soup = BeautifulSoup(request_data, 'html.parser')
        content_div = soup.find('div', class_='mw-category-columns')

        for raw in content_div.select('li'):
            first_letter = raw.a.text[0]

            alphabet_counter[first_letter] += 1
        next_url = soup.find('a', string='Следующая страница')
        if next_url is None:
            break
        url = "https://ru.wikipedia.org" + next_url.get('href')
        logging.info(
            f'Статус подключения: {request.status_code},'
            f' добавленные буквы: {[key for key in alphabet_counter]}')

    with open('beasts.csv', 'a', encoding='UTF-8') as b:
        for letter, count in sorted(alphabet_counter.items(),
                                    key=lambda x: (x[0].isascii(), x[0])):
            b.write(f'{letter}, {count}\n')


if __name__ == "__main__":
    parse_animals_count(URL)
