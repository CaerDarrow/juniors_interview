import re

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from collections import defaultdict
import aiofiles


async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    animals_count = defaultdict(int)

    async with aiohttp.ClientSession() as session:
        while True:
            page_content = await fetch_page(session, url)
            soup = BeautifulSoup(page_content, 'html.parser')
            # итерируюсь по элементам с животными
            for item in soup.select(".mw-category-group ul li a"):
                animal_name = item.get_text().strip()
                first_letter = animal_name[0].upper()

                # пропускаем не русские буквы
                if not re.match("[А-ЯЁ]", first_letter):
                    continue

                animals_count[first_letter] += 1
            #ищем следующую страницу
            next_page = soup.select_one("a:contains('Следующая страница')")
            if next_page:
                url = 'https://ru.wikipedia.org' + next_page.get('href')
            else:
                break

    async with aiofiles.open('beasts.csv', mode='w', encoding='utf-8') as csvfile:
        for letter, count in sorted(animals_count.items()):
            await csvfile.write(f"{letter},{count}\n")


if __name__ == '__main__':
    asyncio.run(main())
