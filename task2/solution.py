import sys

import requests
import csv

from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
            'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']


def parser_launch(url: str, start_letter: str = None, stop_letter: str = None) -> dict:
    alphabet = {}
    list_area = ALPHABET
    if start_letter and start_letter != 'А':
        list_area = list_area[list_area.index(start_letter):]
        url = f"https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from={start_letter}"
    if stop_letter:
        list_area = list_area[:(list_area.index(stop_letter)+1)]
    search_area = [list_area, set(list_area)]
    return wiki_animals_parsing(alphabet, url, search_area)


def write_down(alphabet, search_area) -> None:
    with open("beasts.csv", 'w') as f:
        fieldnames = ['letter', 'quantity']
        for letter in search_area[0]:
            if alphabet.get(letter):
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow({'letter': letter, 'quantity': str(alphabet[letter])})
    return None


def wiki_animals_parsing(alphabet: dict, url: str, search_area: list[list[str], set[str]]) -> dict:
    exit_parser = False
    contents = requests.get(url).text
    soup = BeautifulSoup(contents, 'html.parser')
    content_div = soup.find('div', attrs={'class': 'mw-category-columns'})

    for raw in content_div.select('li'):
        first_letter = raw.a.text[0]
        if first_letter not in search_area[1]:
            write_down(alphabet, search_area)
            exit_parser = True
            break
        else:
            if alphabet.get(first_letter):
                alphabet[first_letter] += 1
            else:
                alphabet.setdefault(first_letter, 1)
    next_url = soup.find('a', string='Следующая страница')
    del contents, soup, content_div
    if next_url is not None and not exit_parser:
        wiki_animals_parsing(alphabet, "https://ru.wikipedia.org" + next_url.get('href'), search_area)
    return alphabet


# parser_launch(URL, "А", "Я")
parser_launch(URL)