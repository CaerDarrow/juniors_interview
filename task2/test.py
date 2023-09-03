import asyncio
from collections import Counter

from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup
from solution import get_count_of_animals, get_next_page
import pathlib


async def test_count_animals_on_page():
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        animals_counter = Counter()
        base_dir = pathlib.Path(__file__).parent.resolve()
        with open(f'{base_dir}/index.html') as f:
            page = f.read()
        soup = BeautifulSoup(page, 'html.parser')
        count_of_animals = await get_count_of_animals(soup)
        animals_counter.update(count_of_animals)

        assert animals_counter.total() == 200


async def test_get_next_page():
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        base_dir = pathlib.Path(__file__).parent.resolve()
        with open(f'{base_dir}/index.html') as f:
            page = f.read()
        soup = BeautifulSoup(page, 'html.parser')
        next_page = await get_next_page(soup)
        assert next_page == "/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:\
%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_\
%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=\
%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%B1%D0%B0%D1%80%D1%81%D1%83%D0%BA#mw-pages"


async def test_all():
    await test_count_animals_on_page()
    await test_get_next_page()


if __name__ == '__main__':
    asyncio.run(test_all())
