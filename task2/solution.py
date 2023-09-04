#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import unittest
import os


def parse_animals_from_wiki() -> None:
    """
    Creates a csv file filled with Russian alphabet letters
    and the number of animals whose names start with the corresponding letter.
    """
    base_url = 'https://ru.wikipedia.org/'
    relative_url = 'w/index.php?title=Категория:Животные_по_алфавиту'
    letter = 'А'
    animal_amount = 0

    with open('beasts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Run cycle while letter in range of uppercase russian letters from A to Я.
        while 1040 <= ord(letter) <= 1071:
            url = base_url + relative_url

            response = requests.get(url)

            if response.status_code != 200:
                raise ValueError(f'URL {url} returned status code: {response.status_code}.')

            page_html = BeautifulSoup(response.content, 'html.parser')
            animal_groups = page_html.find(id='mw-pages').find_all('div', class_='mw-category-group')

            for group in animal_groups:
                group_letter = group.h3.string
                animal_links_num = len(group.find_all('a', href=True))

                if group_letter == letter:
                    # Increment the animal_amount if letter hasn't changed.
                    animal_amount += animal_links_num
                else:
                    # Write data, update letter and set new value to the animal_amount
                    writer.writerow([letter, animal_amount])
                    letter = group_letter
                    animal_amount = animal_links_num

            # Get next page relative url
            next_page_link = page_html.find('a', string='Следующая страница')
            relative_url = next_page_link.get('href') if next_page_link else ''

    return None


parse_animals_from_wiki()


class ParseAnimalsFromWikiTests(unittest.TestCase):
    def setUp(self) -> None:
        with open('beasts.csv', 'r', encoding='utf-8') as f:
            pass

    def test_beasts_csv_created(self):
        self.assertTrue('beasts.csv', os.path.exists('beasts.csv'))

    def test_file_is_not_empty_and_contains_valid_content(self):
        with open('beasts.csv', 'r', encoding='utf-8') as f:
            for line in f:
                letter, animal_amount = line.split(',')
                self.assertIn(ord(letter), range(1040, 1072))
                self.assertGreater(int(animal_amount), 0)

            f.seek(0)
            line = f.readline()
            self.assertTrue(line)


if __name__ == '__main__':
    unittest.main()
