import sys
from collections import Counter
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

alphabet = []

def main(URL):

    contents = requests.get(URL).text

    soup = BeautifulSoup(contents, 'html.parser')

    content_div = soup.find('div', attrs = {'class':'mw-category-columns'})

    for raw in content_div.select('li'):
        first_letter = raw.a.text[0]
        if first_letter == 'A':
            count = Counter(alphabet)
            sorted_alphabet = dict(sorted(count.items()))

            with open('beasts.csv', 'w', newline='',encoding='utf-8') as file:
                writer = csv.writer(file)
                for letter, count in sorted_alphabet.items():
                    writer.writerow([letter, count])
            sys.exit()
        else:
            
            alphabet.append(first_letter)
    next_url = soup.find('a', string='Следующая страница')
    main("https://ru.wikipedia.org" + next_url.get('href'))

main(URL)