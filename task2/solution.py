import csv
import re

import requests
from bs4 import BeautifulSoup 
from fake_headers import Headers


def write_beasts():
    result = dict()
    base_url = 'https://ru.wikipedia.org'
    link = '/wiki/Категория:Животные_по_алфавиту'
    headers = Headers(os='windows', browser='chrome').generate()
    is_continue = True
    while is_continue:
        page = requests.get(url=base_url+link, headers=headers).text
        soup = BeautifulSoup(page, 'lxml')
        category_columns = soup.find('div', attrs={'class': 'mw-category mw-category-columns'})
        category_groups = category_columns.find_all('div', attrs={'class': 'mw-category-group'})
        for group in category_groups:
            key = group.find('h3').text
            if re.match(r'[А-Я]', key) is None:
                is_continue = False
                break
            items_count = len(group.find_all('li'))
            if key in result.keys():
                result[key] = result[key] + items_count
            else:
                result.setdefault(key, items_count)
        link = soup.find(name='a', string=re.compile('Следующая страница')).attrs['href']
    with open('beasts.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for item in result.items():
            writer.writerow(item)