import asyncio
import httpx
import sys
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

ans_for_csv = dict()
is_english_letters = False


async def get_all_info_for_letter(url: str, from_letters: str):
    send_url = url + f"&from={from_letters[0]}"
    response = await asyncio.to_thread(httpx.get, send_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h3 = soup.find_all('div', class_='mw-category mw-category-columns')
    list_animals = []
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
                words = animal.split()
                if len(words) == 1:
                    ans_for_csv[animal[0]] = ans_for_csv.get(animal[0], 0) + 1
                else:
                    ans_for_csv[words[-1][0].upper()] = ans_for_csv.get(words[-1][0].upper(), 0) + 1
                list_animals.append(animal)
    if c == 200:
        find_link_next_page = soup.find_all('div', id='mw-pages')
        a_tags = find_link_next_page[0].find_all('a')
        link = "https://ru.wikipedia.org" + a_tags[-1].get('href')
        next_page_info = await get_all_info_for_letter(link, from_letters)
        list_animals.extend(next_page_info)
    return list_animals  # в этом решении еще можно для каждой буквы в task.result() увидеть список животных


async def main():
    tasks = []
    for start_letters in range(ord('А'), ord('Я') + 1):
        tasks.append(asyncio.create_task(get_all_info_for_letter(url, chr(start_letters))))
    if is_english_letters:
        for start_letters in range(ord('A'), ord('Z') + 1):
            tasks.append(asyncio.create_task(get_all_info_for_letter(url, chr(start_letters))))
    await asyncio.gather(*tasks)
    csv_f = open("beasts.csv", "a+")
    for i in sorted(ans_for_csv.keys()):
        row = f"{i},{ans_for_csv[i]}\n"
        csv_f.write(row)


"""
Разница в том, что здесь решение будет работать гораздо быстрее, но терять порядка 500 животных, потому что
у Википедии есть проблемы со структурированием данных при пролистывании страниц, поэтому здесь чуть по-другому работает
Например, в английских буквах при пролистывании встречается русская М и это не фиксится при работе именно здесь,
в асинхронном состоянии, когда мы делаем запрос с ключом from=М, например.
Эта проблема фиксится при синхронном обходе всех страниц подряд.
При асинхронном подходе нам не нужно будет ждать ответа для следующих действий, мы можем просто отложить пока работу
текущей функции и заняться другим запросом.
"""
if __name__ == "__main__":
    if "-eng" in sys.argv:
        is_english_names = True
    asyncio.run(main())
