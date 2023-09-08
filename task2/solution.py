import requests
from bs4 import BeautifulSoup
import csv
import unittest
from io import StringIO
import sys
import os
from scrape_wikipedia import scrape_and_write_to_csv

url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    category_groups = soup.find_all(class_='mw-category-group')
    alphabet_counts = {}
    for category_group in category_groups:
        category_list_items = category_group.find_all('li')
        for category_item in category_list_items:
            category_text = category_item.text.strip()
            first_letter = category_text[0].upper()
            if first_letter in alphabet_counts:
                alphabet_counts[first_letter] += 1
            else:
                alphabet_counts[first_letter] = 1
    with open('beasts.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Буква', 'Количество'])
        for letter, count in alphabet_counts.items():
            csv_writer.writerow([letter, count])

    print("Данные успешно записаны в файл beasts.csv")
else:
    print("Не удалось получить доступ к странице")


class TestScrapeWikipedia(unittest.TestCase):
    def test_scrape_and_write_to_csv(self):
        sys.stdout = StringIO()
        scrape_and_write_to_csv()
        sys.stdout = sys.__stdout__
        self.assertTrue(os.path.isfile('beasts.csv'))
        self.assertTrue(os.path.getsize('beasts.csv') > 0)
        os.remove('beasts.csv')


if __name__ == '__main__':
    unittest.main()
