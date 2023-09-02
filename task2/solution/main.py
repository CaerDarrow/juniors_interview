import asyncio, csv, re, bs4, aiohttp, collections, aiofiles, aiocsv


async def get_animals(page: bs4.BeautifulSoup) -> dict[str, int]:
    counter = {}
    all_groups = page.find_all('div', class_='mw-category-group')
    
    for group in all_groups:
        char = group.find('h3').text
        counter[char] = len(group.find_all('a', href=re.compile(f'{char}*')))
    return counter


async def get_page(session: aiohttp.ClientSession, url: str) -> bytes:
    async with session.get(url) as response:
        return await response.read()


async def write_data(data: list):
    async with aiofiles.open("beasts.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = aiocsv.AsyncWriter(file, dialect="unix")
        await writer.writerows(data)
        

async def get_next_page(page: bs4.BeautifulSoup) -> str:
    try:
        next_page = page.find('a', string=re.compile('Следующая страница')).get('href')
        return next_page
    except AttributeError:
        return None
    
    
async def main() -> None:
    animals_counter = collections.Counter()
    bas_url = 'https://ru.wikipedia.org/'
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    page = await get_page(session, url)
    soup = bs4.BeautifulSoup(page, 'html.parser')

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        while True:
            mw_pages = soup.find('div', id='mw-pages')
            
            animals_counter.update(get_count_of_animals_page(animals_counter, session, url))
            next_page = await get_next_page(soup, mw_pages)
            
            if not next_page:
                break
            
            url = bas_url + next_page
            
        char_animal_list = sorted(animals_counter.items())
        await write_data(char_animal_list)


async def get_count_of_animals_page(session: aiohttp.ClientSession, url: str):
    page = await get_page(session, url)
    soup = bs4.BeautifulSoup(page, 'html.parser')

    return await get_animals(soup, page)


if __name__ == '__main__':
    asyncio.run(main())
    
