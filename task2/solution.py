from bs4 import BeautifulSoup
import csv
import asyncio
import aiohttp


file_name = 'beasts.csv'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

all_letters = [chr(i) for i in range(ord("А"), ord("А") + 32)]
animals_count = {i: 0 for i in all_letters}


async def get_page_data(session, letter):
    letter_url = f"https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from={letter}"
    flag = True

    while flag:
        async with session.get(url=letter_url, headers=headers) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'lxml')
            block = soup.find('div', class_='mw-category mw-category-columns')
            categories_group = block.find_all('div', class_='mw-category-group')

            for category in categories_group:
                category_letter = category.find_next('h3').text
                if category_letter != letter:
                    flag = False
                    break
                count_words = len(category.find_all('li'))

                if category_letter not in animals_count:
                    raise KeyError(f"Категория '{category_letter}' не инициализирована в словаре.")

                animals_count[category_letter] += count_words

            if flag:
                links = soup.find('div', id='mw-pages').find_all('a')
                for a in links:
                    if a.text == 'Следующая страница':
                        next_page_url = 'https://ru.wikipedia.org/' + a.get('href')
                        letter_url = next_page_url
                        break

        print("Парсинг буквы", letter)


async def gather_data():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for letter in all_letters:
            task = asyncio.create_task(get_page_data(session, letter))
            tasks.append(task)

        await asyncio.gather(*tasks)


def main():
    asyncio.get_event_loop().run_until_complete(gather_data())

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        for key, value in animals_count.items():
            if value != 0:
                writer.writerow((key,value))


if __name__ == '__main__':
    main()
    print('\n', 'Парсинг завершен.')