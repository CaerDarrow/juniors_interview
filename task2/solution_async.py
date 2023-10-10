import asyncio
import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict


result = defaultdict(set)


async def load_animal_data(session: aiohttp.ClientSession, url: str):
    async with session.get(url, ssl=False) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        div = soup.find('div', attrs={'class': 'mw-category mw-category-columns'})
        h3 = div.find('h3')
        lis = [x.text for x in div.findAll('li')]
        lis = list(filter(lambda x: x[0] == h3.text, lis))
        result[h3.text.upper()] = result[h3.text.upper()].union(lis)


async def load_data():
    url = "http://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        main_page = await session.get(url, ssl=False)
        soup = BeautifulSoup(await main_page.text(), 'lxml')
        hrefs = []
        table = soup.find('div', attrs={'class': 'mw-parser-output'})
        links = table.findAll('a')
        for link in links:
            if link['href'].startswith('https'):
                hrefs.append(link['href'])
                task = asyncio.create_task(load_animal_data(session, link['href']))
                tasks.append(task)
        print(hrefs)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(load_data())
    for letter in result:
        print(letter, len(result[letter]))
