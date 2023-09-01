import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv


async def process_animal_page(session, url, animal_counts):
    async with session.get(url) as response:
        if response.status == 200:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            animal_links = soup.find_all("div", class_="mw-category-group")

            for group in animal_links:
                letter = group.find("h3").text
                animals = group.find_all("a")
                count = len(animals)

                if letter in animal_counts:
                    animal_counts[letter] += count
                else:
                    animal_counts[letter] = count

            next_page_link = soup.find("a", text="Следующая страница")

            if next_page_link:
                next_page_url = "https://ru.wikipedia.org" + next_page_link["href"]
                print(next_page_url)
                await process_animal_page(session, next_page_url, animal_counts)
        else:
            print(f"Ошибка при отправке запроса к {url}")


async def main():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    animal_counts = {}

    async with aiohttp.ClientSession() as session:
        await process_animal_page(session, url, animal_counts)

    with open("beasts.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for letter, count in animal_counts.items():
            writer.writerow([letter, count])

    print("Данные успешно записаны в beasts.csv")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
