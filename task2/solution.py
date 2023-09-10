import requests
from bs4 import BeautifulSoup
import csv


letter_count = {}# общий счетчик букв
base_url = 'https://ru.wikipedia.org'# базовый урл
url = '/wiki/Категория:Животные_по_алфавиту'# относительный урл, берем из следующий страницы

while True:

    r = requests.get(base_url + url)

    page_content = r.text

    soup = BeautifulSoup(page_content, 'html.parser')

    beasts = soup.find('div', class_='mw-category mw-category-columns') #считываю нужную часть
    pa = soup.find(id='mw-pages')
    li_tags = beasts.find_all('li')# все животные на одной странице

    for l in li_tags:
        beast = l.text.strip()
        if beast[0] not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
            with open('beasts.csv', 'w', encoding='utf-8', newline='') as file_obj:
                fieldnames = ['Буква', 'Количество']
                writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

                writer.writeheader()
                for letter, count in sorted(letter_count.items()):
                    writer.writerow({'Буква': letter, 'Количество': count})

            print("Результат записан в файл beasts.csv")
            exit()
        letter_count[beast[0]] = letter_count.get(beast[0], 0) + 1# счетчик, если буква не найдена, создается новый элем со знач 0

    link_next_page = pa.find_all('a')[-1]# относительная ссылка на следующую страницу
    url = link_next_page.get('href')
