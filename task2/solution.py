import csv

import requests
from bs4 import BeautifulSoup

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
animals = {letter: 0 for letter in alphabet}

base = 'https://ru.wikipedia.org'
page = '/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'

flag = True

while flag:
    r = requests.get(base + page)
    soup = BeautifulSoup(r.text, 'html.parser')
    groups = soup.find_all('div', class_='mw-category mw-category-columns')
    groups = groups[0].find_all('div', class_='mw-category-group')
    for group in groups:
        letter = group.find('h3').text
        if letter in animals:
            animals[letter] += len(group.find_all('li'))
        else:
            flag = False
    page = soup.find('a', string='Следующая страница')['href']

with open('animals.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for row in animals.items():
        writer.writerow(row)
