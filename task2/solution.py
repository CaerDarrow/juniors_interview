import asyncio
import csv
from dataclasses import dataclass

import aiohttp
import requests
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(module)s [%(name)s:%(lineno)s] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
)
logger = logging.getLogger('solution')


@dataclass
class Constants:
    URL: str = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    RESULT_FILE_NAME: str = 'beasts.csv'
    ENG_LETTER_A: str = 'A'
    FROM_SECOND_LINE: int = 1
    FIRST_LETTER_ID: int = 0


def get_soup_from_request(request_url: str) -> bs:
    request = requests.get(url=request_url)
    soup = bs(request.content, 'html.parser')

    return soup


def get_table_lines_from_soup(soup_data) -> ResultSet:
    table_ = soup_data.find('table', class_='plainlinks')
    lines = table_.find_all('tr')

    return lines


def get_letter_links(table_lines) -> set[str]:
    links_list = set()

    for line in table_lines[Constants.FROM_SECOND_LINE:]:
        links = line.find_all('a')
        {links_list.add(link['href']) for link in links}

    return links_list


async def get_animals_from_pages(links: set[str]) -> list[set]:
    async with aiohttp.ClientSession() as session:
        requests_ = [get_data(url, session) for url in links]
        result = await asyncio.gather(*requests_, return_exceptions=False)

    return result


async def get_data(url: str, session: ClientSession) -> set[str]:
    async with session.get(url, ssl=False) as response:
        result = set()

        if response.status == 200:
            soup = bs(await response.text(), 'html.parser')
            links = soup.find_all('div', class_='mw-category mw-category-columns')

            for link in links:
                letter = link.find('h3').text
                if letter == Constants.ENG_LETTER_A:
                    break

                animals = link.find_all('a')
                {result.add(a.text) for a in animals}

        return result


def handle_data(data: list[set]):
    result = _create_result_dict()
    union_data = _union_sets_with_animals(data=data)

    for name in union_data:
        letter = name[Constants.FIRST_LETTER_ID]
        if letter == Constants.ENG_LETTER_A:
            continue
        result[letter] = result.get(letter) + 1 if result.get(letter) is not None else 1

    return result


def _create_result_dict() -> dict[str, int]:
    start = ord('а')
    return {chr(i).upper(): 0 for i in range(start, start + 32)}


def _union_sets_with_animals(data: list[set]) -> set:
    return set().union(*data)


def create_csv_file(file_name: str, results: dict[str, int]) -> None:
    with open(file_name, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        [writer.writerow([letter, count]) for letter, count in results.items()]


async def main() -> None:
    logger.info('Start program')

    soup = get_soup_from_request(request_url=Constants.URL)
    logger.info(f'Got soup from {Constants.URL}')

    table_lines = get_table_lines_from_soup(soup_data=soup)
    logger.info('Got table data from soup')

    letter_links = get_letter_links(table_lines=table_lines)
    logger.info('Got letter links from table data')

    data = await get_animals_from_pages(links=letter_links)
    logger.info('Got animals from wiki')

    animals_count = handle_data(data=data)
    logger.info('Handled animals')

    create_csv_file(file_name=Constants.RESULT_FILE_NAME, results=animals_count)
    logger.info('Created csv file with results')


if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)
    asyncio.run(main())
