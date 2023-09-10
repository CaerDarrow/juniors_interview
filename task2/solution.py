"""2. Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv
количество животных на каждую букву алфавита. Содержимое результирующего файла:

А,642
Б,412
В,....

Примечание:
анализ текста производить не нужно, считается любая запись из категории
(в ней может быть не только название, но и, например, род)."""

import requests
from bs4 import BeautifulSoup
import csv


def get_animals_from_page(url: str) -> tuple:
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')
    animal_links = soup.find(id='mw-pages').find(class_='mw-content-ltr').findChildren('a')
    animal_names = [link.text for link in animal_links]
    all_links = soup.findAll('a')
    next_page_links = [link for link in all_links if link.text == 'Следующая страница']
    next_page_url = None
    if len(next_page_links) > 0:
        link = next_page_links[-1]
        if link['href']:
            next_page_url = link['href']
    return (animal_names, next_page_url)


def get_animals_count(page_url: str, url_prefix: str) -> dict:
    count_dict = {}
    while page_url is not None:
        animals, next_page_url = get_animals_from_page(page_url)
        for animal in animals:
            first_letter = animal[0].upper()
            count_dict.setdefault(first_letter, 0)
            count_dict[first_letter] += 1
        if next_page_url is not None and not next_page_url.startswith('http'):
            next_page_url = url_prefix + next_page_url
        page_url = next_page_url
    return count_dict


# print(count_dict)


def write_to_file(count_dict: dict, file_name: str):
    with open(file_name, 'w', encoding="UTF-8", newline="") as f:
        csv_writer = csv.writer(f)
        rows = []
        for letter in sorted(count_dict):
            row = (letter, count_dict[letter])
            rows.append(row)
        csv_writer.writerows(rows)


def save_animal_list(page_url: str, page_prefix: str, file_path: str):
    x = get_animals_count(page_url, page_prefix)
    write_to_file(x, file_name=file_path)