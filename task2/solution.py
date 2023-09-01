import asyncio
import csv
import re
from collections import Counter

from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup


async def get_page(session: ClientSession, url: str) -> bytes:
    async with session.get(url) as response:
        return await response.read()


async def get_count_of_animals(soup: BeautifulSoup) -> dict[str, int]:
    mw_pages = soup.find('div', id='mw-pages')
    animals_counter = {}
    all_groups = mw_pages.find_all('div', class_='mw-category-group')
    for group in all_groups:
        main_char = group.find('h3').text
        animals_links = group.find_all('a', href=re.compile(f'{main_char}*'))
        animals_counter[main_char] = len(animals_links)
    return animals_counter


async def get_next_page(soup: BeautifulSoup) -> str:
    try:
        mw_pages = soup.find('div', id='mw-pages')
        next_page = mw_pages.find('a', string=re.compile('Следующая страница')).get('href')
        return next_page
    except AttributeError:
        return None


def write_data(data: list):
    with open('beasts.csv', 'w+', newline='') as csvfile:
        csvfile.truncate()
        writer = csv.writer(csvfile)
        writer.writerows(data)


async def main() -> None:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        animals_counter = Counter()
        bas_url = 'https://ru.wikipedia.org/'
        url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        while True:
            page = await get_page(session, url)
            soup = BeautifulSoup(page, 'html.parser')
            count_of_animals = await get_count_of_animals(soup)
            animals_counter.update(count_of_animals)
            next_page = await get_next_page(soup)
            if not next_page:
                break
            url = bas_url + next_page
        char_animal_list = sorted(animals_counter.items())
        write_data(char_animal_list)


async def test_count_animals_on_page():
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        animals_counter = Counter()
        url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        page = await get_page(session, url)
        soup = BeautifulSoup(page, 'html.parser')
        count_of_animals = await get_count_of_animals(soup)
        animals_counter.update(count_of_animals)

        assert animals_counter.total() == 200

        bas_url = 'https://ru.wikipedia.org/'
        next_page = await get_next_page(soup)
        url = bas_url + next_page
        page = await get_page(session, url)
        soup = BeautifulSoup(page, 'html.parser')
        count_of_animals = await get_count_of_animals(soup)
        animals_counter.update(count_of_animals)

        assert animals_counter.total() == 400


if __name__ == '__main__':
    asyncio.run(test_count_animals_on_page())
    asyncio.run(main())
