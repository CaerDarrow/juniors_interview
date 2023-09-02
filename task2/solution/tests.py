import asyncio, bs4, aiohttp, collections
from main import (
    get_page, get_animals, get_next_page
)

async def count_of_animals(session: aiohttp.ClientSession, url:str):
    page = await get_page(session, url)
    soup = bs4.BeautifulSoup(page, 'html.parser')
    return await get_animals(soup)
    
    
async def test_count_animals_on_page():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        animals_counter = collections.Counter()
        url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

        animals_counter.update(count_of_animals(session, url))

        assert animals_counter.total() == 200
        
        page = await get_page(session, url)
        soup = bs4.BeautifulSoup(page, 'html.parser')
        bas_url = 'https://ru.wikipedia.org/'
        
        next_page = await get_next_page(soup)
        url = bas_url + next_page
        animals_counter.update(count_of_animals(session, url))

        assert animals_counter.total() == 400


if __name__ == "__main__":
    asyncio.run(test_count_animals_on_page())
