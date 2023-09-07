import csv
import pathlib
import re
import time
from collections import Counter
from functools import wraps

import requests
from bs4 import BeautifulSoup

import logging

# Параметры логирования
logging.basicConfig(filename="py_log.log",
                    filemode="w",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
parsing_logger = logging.getLogger(__name__)

base_dir = pathlib.Path(__file__).parent.resolve()


# Функция декоратор замера времени выполнения функции
def log_time(logger, description=''):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            logger.info(f'Start parsing {description} ({func.__name__})')
            result = func(*args, **kwargs)
            end = time.time()
            exec_time = round(end - start, 2)
            logger.info(f'Parsing time {description} ({func.__name__}): {exec_time}s')
            return result

        return wrapper

    return inner


def get_page(session, url: str) -> bytes:
    response = session.get(url)
    return response.content


def get_count_of_animals(soup: BeautifulSoup) -> dict[str, int]:
    mw_pages = soup.find('div', id='mw-pages')
    animals_counter = {}

    # получаем раздел со всеми группами букв в нём (А:..., Б:...) и в каждом ведём подсчёт
    all_groups = mw_pages.find_all('div', class_='mw-category-group')
    for group in all_groups:
        main_char = group.find('h3').text
        print(main_char)
        animals_links = group.find_all('a', string=re.compile(f'{main_char}.+'))
        animals_counter[main_char] = len(animals_links)

    return animals_counter


def get_next_page(soup: BeautifulSoup) -> str | None:
    try:
        mw_pages = soup.find('div', id='mw-pages')
        next_page = mw_pages.find('a', string=re.compile('Следующая страница')).get('href')
        return next_page
    except AttributeError:
        return None


def write_data(saving_path, data: list):
    with open(saving_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


@log_time(logger=parsing_logger)
def main() -> None:
    bas_url = 'https://ru.wikipedia.org/'
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    animals_counter: Counter = Counter()

    while True:
        session = requests.Session()

        page = get_page(session, url)
        soup = BeautifulSoup(page, 'html.parser')
        count_of_animals = get_count_of_animals(soup)

        animals_counter.update(count_of_animals)
        next_page = get_next_page(soup)
        if not next_page:
            break
        url = bas_url + next_page
    print(animals_counter.total())

    return animals_counter


if __name__ == '__main__':
    saving_path = base_dir / 'beasts.csv'

    animals_counter = main()
    char_animal_list = sorted(animals_counter.items())
    write_data(saving_path, char_animal_list)

# without session
# 2023-09-07 18:30:29,870 - __main__ - INFO - Start parsing  (main)
# 2023-09-07 18:31:23,610 - __main__ - INFO - Parsing time  (main): 53.74s

# with session before cache
# 2023-09-07 18:34:34,892 - __main__ - INFO - Start parsing  (main)
# 2023-09-07 18:35:28,676 - __main__ - INFO - Parsing time  (main): 53.78s

# with session after cache
# 2023-09-07 18:36:13,615 - __main__ - INFO - Start parsing  (main)
# 2023-09-07 18:37:07,343 - __main__ - INFO - Parsing time  (main): 53.73s

