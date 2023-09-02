import sys
from collections import Counter
import requests
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
alphabet = []


def wikiAnimalsParsing(URL):
    contents = requests.get(URL).text
    soup = BeautifulSoup(contents, 'html.parser')
    content_div = soup.find('div', attrs={'class': 'mw-category-columns'})
    for raw in content_div.select('li'):
        first_letter = raw.a.text[0]
        if first_letter == 'A':
            count = Counter(alphabet)
            sorted_alphabet = dict(sorted(count.items()))
            for letter, v in sorted_alphabet.items():
                with open('beasts.csv', 'a', encoding='UTF-8') as b:
                    b.write(f'{letter}, {v} \n')
            sys.exit()
        else:
            alphabet.append(first_letter)
    next_url = soup.find('a', text='Следующая страница')
    wikiAnimalsParsing("https://ru.wikipedia.org" + next_url.get('href'))


wikiAnimalsParsing(URL)
