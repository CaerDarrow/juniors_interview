from constants import DOMAIN_WIKI, RUSSIAN_LETTERS, START_URL
from collections import defaultdict
from string import ascii_uppercase

from bs4 import BeautifulSoup
from requests import Session
import csv

class NextPageDoesNotExists(Exception):
    ...

job = Session()


def write_data_to_csv(data: defaultdict) -> None:
    """Write data to csv"""

    with open("beasts.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(("Letter", "Count"))
        for letter in RUSSIAN_LETTERS:
            w.writerow((letter, data[letter]))


class AnimalData:
    COUNT_ANIMALS_BY_LETTER = defaultdict(int)

    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_next_page_url(soup: BeautifulSoup) -> str:
        """Search next page"""

        next_page_button = soup.find_all(
            "a", {"title": "Категория:Животные по алфавиту"}
        )[1]
        if next_page_button.text != "Следующая страница":
            raise NextPageDoesNotExists()
        next_page_url = f'{DOMAIN_WIKI}{next_page_button.get("href")}'
        return next_page_url

    def get_page_data(self, url: str) -> None:
        """
        Получение данных со страницы, поиск блока
        с животными, подсчет колличества.
        """

        response = job.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        animals = soup.find("div", class_="mw-content-ltr").find_all("li")[2:]
        for animal in animals:
            first_letter = animal.text[0]
            if first_letter in ascii_uppercase:
                return
            self.COUNT_ANIMALS_BY_LETTER[first_letter] += 1
        try:
            next_page_url = self.get_next_page_url(soup)
        except NextPageDoesNotExists:
            return
        self.get_page_data(next_page_url)

    def __call__(self) -> defaultdict[str, int]:
        self.get_page_data(self.url)
        return self.COUNT_ANIMALS_BY_LETTER


def main():
    animal_data = AnimalData(START_URL)
    result = animal_data()
    write_data_to_csv(result)


if __name__ == "__main__":
    main()