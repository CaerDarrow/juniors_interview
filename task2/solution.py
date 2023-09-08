import asyncio
import csv
import pathlib
import re
import time
from collections import Counter
from functools import wraps

from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup

import logging

'''
Почему асинхронный код работает в данном случае быстрее?
Если он вызывается по сути везде последовательно.
aiohttp оптимизированнее, чем requests? 

Уточнить данный вопрос на курсе или у Тетрики (Андрея)
'''

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


async def get_page(session: ClientSession, url: str) -> bytes:
    async with session.get(url) as response:
        return await response.read()


async def get_count_of_animals(soup: BeautifulSoup) -> dict[str, int]:
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


async def get_next_page(soup: BeautifulSoup) -> str | None:
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


async def main_async() -> None:
    bas_url = 'https://ru.wikipedia.org/'
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        animals_counter: Counter = Counter()

        while True:
            page = await get_page(session, url)
            soup = BeautifulSoup(page, 'html.parser')
            count_of_animals = await get_count_of_animals(soup)

            animals_counter.update(count_of_animals)
            next_page = await get_next_page(soup)
            if not next_page:
                break
            url = bas_url + next_page
        print(animals_counter.total())

    return animals_counter


@log_time(logger=parsing_logger)
def main(saving_path):
    animals_counter = asyncio.run(main_async())

    char_animal_list = sorted(animals_counter.items())
    write_data(saving_path, char_animal_list)


if __name__ == '__main__':
    saving_path = base_dir / 'beasts.csv'

    main(saving_path)

# before cache
# 2023-09-07 18:13:40,569 - __main__ - INFO - Start parsing  (main)
# 2023-09-07 18:15:19,055 - __main__ - INFO - Parsing time  (main): 98.49s

# after cache
# 2023-09-04 19:14:26,985 - __main__ - INFO - Start parsing  (main)
# 2023-09-04 19:14:47,776 - __main__ - INFO - Parsing time  (main): 20.79s


