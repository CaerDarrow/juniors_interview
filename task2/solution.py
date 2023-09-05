import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv


def write_beasts(beasts_dict: dict) -> None:
    try:
        with open('beasts.csv', 'w', encoding='utf-8', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(beasts_dict.items())
    except IOError:
        print('I/O error')


def parse_beasts() -> dict:
    output = {}
    page_url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0' \
               '%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    while True:
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        areas = soup.select('.mw-category-columns > div')
        for area in areas:
            letter = area.find('h3').text
            if letter == 'A':
                return output
            count_articles = len(area.find_all('li'))
            if letter not in output.keys():
                output.update({letter: count_articles})
            else:
                output[letter] += count_articles
        next_page_elem = soup.find('a', string='Следующая страница')
        next_page_relative_link = next_page_elem.get('href')
        next_page_absolute_link = urllib.parse.urljoin(page_url, next_page_relative_link)
        page_url = next_page_absolute_link


if __name__ == '__main__':
    beasts = parse_beasts()
    write_beasts(beasts)
