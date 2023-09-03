import sys
import os
import csv
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from progress.counter import Counter
from requests_cache.models.response import OriginalResponse
from requests_cache.session import CachedSession

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from task2.mock_settings import is_mock
from tests_task2.conftest import START_URL, get_response_mock

URL: str = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
BASE_DIR: Path = Path(__file__).parent
amount_animals: dict = {}
counter = Counter(message='parsing page ')


def get_response(
        session: CachedSession, url: str) -> Optional[OriginalResponse]:
    response = session.get(url)
    response.encoding = 'utf-8'
    counter.next()
    return response


if is_mock:
    get_response = get_response_mock
    URL = START_URL


def calculate_beasts(session: CachedSession, url: str) -> list[str]:
    '''
    Получает с русскоязычной википедии список всех животных и заполняет
    словарь с количеством животных на каждую букву алфавита.
    '''
    response = get_response(session, url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, 'lxml')
    mw_pages_id = soup.find('div', attrs={'id': 'mw-pages'})
    ul_tags = mw_pages_id.find('ul')
    a_tags = ul_tags.find_all('a')
    for a_tag in a_tags:
        letter = a_tag['title'][0].upper()
        amount_animals[letter] = amount_animals.get(letter, 0) + 1
    last_a_tag = mw_pages_id.find_all('a')[-1]
    if last_a_tag.text == 'Следующая страница':
        href = last_a_tag['href']
        next_url = urljoin(URL, href)
        calculate_beasts(session, next_url)


def make_file(results: dict[str]) -> None:
    '''Сохраняет данные в файл.'''
    file_name = 'beasts.csv'
    file_path = BASE_DIR / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_NONE)
        writer.writerows(results.items())


def main() -> None:
    '''Главная функция.'''
    session = requests_cache.CachedSession()
    calculate_beasts(session, URL)
    counter.finish()
    make_file(amount_animals)


if __name__ == '__main__':
    main()
