import aiohttp
import asyncio
from bs4 import BeautifulSoup

ROOT_URL = 'https://ru.wikipedia.org'


def get_result(soup):
    tables = soup.find('div', class_='mw-category mw-category-columns').find_all('div', 'mw-category-group')
    next_page = soup.find('a', string='Следующая страница')
    if not next_page:
        return
    for table in tables:
        letter = table.h3.text
        result[letter] = result.get(letter, 0) + len(table.find_all('li'))
        # if letter in result:
        #     result[letter] += len(table.find_all('li'))
        # else:
        #     return
    return ROOT_URL + next_page['href']


async def get_info(session, url):
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        return get_result(soup)


async def main(url):
    async with aiohttp.ClientSession() as session:
        page = await get_info(session, url)
        while page:
            page = await get_info(session, page)
            print(result)


def write_csv(data):
    with open('beasts.csv', 'w', encoding='UTF-8') as file:
        for letter, quantity in result.items():
            file.write(f'{letter},{quantity}\n')


if __name__ == "__main__":
    # result = dict.fromkeys(list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)
    result = {}
    asyncio.run(main('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'))
    write_csv(result)


