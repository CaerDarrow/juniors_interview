import time

import httpx, asyncio
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

ans_for_csv = dict()


async def func1(url: str, from_letters: str, english_letter: bool):
    send_url = url + f"&from={from_letters[0]}"
    response = await asyncio.to_thread(httpx.get, send_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h3 = soup.find_all('div', class_='mw-category mw-category-columns')
    list_animals = []
    flag = True
    elements_inside_div = []
    for div_element in h3:
        h3_element = div_element.find('h3')
        if h3_element and h3_element.get_text() == from_letters:
            elements_inside_div = div_element.find_all()
    c = 0
    for elem_h in elements_inside_div[:1]:
        ul = elem_h.find_all('ul')
        for elem_ul in ul[:1]:
            a_tag = elem_ul.find_all('a')
            for elem_a in a_tag:
                animal = elem_a.get_text()
                c += 1
                ans_for_csv[from_letters[0]] = ans_for_csv.get(from_letters[0], 0) + 1
                list_animals.append(animal)
    if c == 200:
        find_link_next_page = soup.find_all('div', id='mw-pages')
        a_tags = find_link_next_page[0].find_all('a')
        link = "https://ru.wikipedia.org" + a_tags[-1].get('href')
        next_page_info = await func1(link, from_letters, english_letter)
        list_animals.extend(next_page_info)
    return list_animals


async def main():
    tasks = []
    start_letters = 'А'
    while start_letters != chr(ord('Я') + 1):
        tasks.append(asyncio.create_task(func1(url, start_letters, False)))
        start_letters = chr(ord(start_letters) + 1)
    await asyncio.gather(*tasks)
    csv_f = open("beasts.csv", "a+")
    for i in sorted(ans_for_csv.keys()):
        row = f"{i},{ans_for_csv[i]}\n"
        csv_f.write(row)
