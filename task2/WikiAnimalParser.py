import constants
import requests

from bs4 import BeautifulSoup
from typing import ItemsView

base_url = 'https://ru.wikipedia.org/'


class WikiAnimalParser(object):
    def __init__(self) -> None:
        self.__counter_animals_by_letter = {}
        self.__page_url = '{}w/index.php?title=Категория:Животные_по_алфавиту'.format(base_url)

    def __try_count_animals_by_link(self, animal_link) -> None:
        current_animals_at_link = animal_link.find_all('div', class_='mw-category-group')

        for animal in current_animals_at_link:
            if animal.h3.string not in constants.russian_alphabet:
                continue
            if animal.h3.string not in self.__counter_animals_by_letter:
                self.__counter_animals_by_letter[animal.h3.string] = 0
            self.__counter_animals_by_letter[animal.h3.string] += len(animal.find_all('a', href=True))

    def __enter__(self):
        while True:
            response = requests.get(self.__page_url)

            if response.status_code != constants.OK:
                response.raise_for_status()

            page_html = BeautifulSoup(response.content, 'html.parser')
            animal_link = page_html.find(id='mw-pages')

            self.__try_count_animals_by_link(animal_link)

            next_page_link = page_html.find('a', string='Следующая страница')
            relative_url = next_page_link.get('href') if next_page_link else 'not found'
            if relative_url == 'not found':
                return self
            self.__page_url = '{}{}'.format(base_url, relative_url)

    def __exit__(self, type, value, traceback):
        if type != None or value != None or traceback != None:
            print("Exiting the context....") 
            print("Type: {}, Value: {}, Traceback: {}".format(type, value, traceback))

    def get_result(self) -> dict:
        return self.__counter_animals_by_letter
