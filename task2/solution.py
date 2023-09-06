from collections import defaultdict
import csv

import requests
from bs4 import BeautifulSoup

base_url = 'https://ru.wikipedia.org'
current_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

count_beasts = defaultdict(int)
allowed_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

while current_url:
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    groups = soup.find("div", class_="mw-category mw-category-columns").find_all("div", class_="mw-category-group")

    for group in groups:
        name_group = group.find("h3").text
        if name_group not in allowed_letters:
            current_url = None
            break
        count_beasts[name_group] += len(group.find_all("li"))

    else:
        for link in soup.find_all('a', href=True):
            if link.text == "Следующая страница":
                link = link['href']
                current_url = base_url + link
                break

with open("beasts.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(count_beasts.items())
