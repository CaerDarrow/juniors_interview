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
        letter = table.h3.text.encode("utf-8")
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


async def start_parsing(url):
    async with aiohttp.ClientSession() as session:
        page = await get_info(session, url)
        while page:
            page = await get_info(session, page)
            print(result)


def write_csv(data):
    with open('beasts.csv', 'w', encoding='utf-8-sig') as file:
        for letter, quantity in result.items():
            file.write(f'{letter.decode("utf-8")},{quantity}\n')


def main():
    global result
    result = {}
    asyncio.run(start_parsing('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'))
    write_csv(result)

if __name__ == "__main__":
    main()



