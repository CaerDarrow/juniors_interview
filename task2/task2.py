import csv

import requests
from bs4 import BeautifulSoup


def pars_data(url):
    data = {}
    flag = True
    while flag:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quote = soup.find_all('div', {'class': 'mw-category-group'})
        for item in quote[2:]:
            letter = item.find_all('h3')[0].text
            if letter.isascii():
                flag = False
                break
            print(f'Смотрим животных на букву : {letter}')
            data[letter] = (
                data.get(letter, 0) +
                len(item.find_all('ul')[0].find_all('li'))
            )
        url = 'https://ru.m.wikipedia.org' + soup.find_all(
            'a', {'title': 'Категория:Животные по алфавиту'}
        )[-1]['href']
    return data


def write_to_csv(filename: str, data: dict) -> None:
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in data.items():
            writer.writerow([key, value])


if __name__ == '__main__':
    data = pars_data('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')
    write_to_csv('beasts.csv', data)
