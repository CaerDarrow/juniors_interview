import asyncio
import csv
import re

from bs4 import BeautifulSoup, Tag
from httpx import AsyncClient


class BeastCounter:
    """Script class for counting beasts and writing data to csv."""

    def __init__(self, result_file_name='beasts.csv') -> None:
        """Inits `BeastCounter` instance."""
        self.URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        self.URL_BASE = 'https://ru.wikipedia.org'
        self.beasts_dict = {}
        self.result_file_name = result_file_name

    async def run_script(self) -> None:
        """Main method to run script."""
        print('Start counting beasts..')
        await self._count_beasts(self.URL)
        print('Beasts counted')

        print('Writing data to csv..')
        self._write_to_csv()
        print('Done!')

    async def _count_beasts(self, url: str) -> None:
        """Counts beasts and writes data to dictionary."""
        soup = await self._get_soup(url)
        animal_columns = soup.select('div.mw-category.mw-category-columns')[0]
        animal_groups = list(animal_columns.children)
        for group in animal_groups:
            animal_first_letter = group.h3.text
            if not re.match(r'[А-Я]', animal_first_letter):
                return

            if animal_first_letter not in self.beasts_dict:
                self.beasts_dict[animal_first_letter] = 0

            group_animals_count = len([elem for elem in list(group.ul.children) if elem != '\n'])
            self.beasts_dict[animal_first_letter] += group_animals_count

        next_page_link = self._get_next_page_link(soup)
        await self._count_beasts(next_page_link)

    async def _get_soup(self, url: str) -> BeautifulSoup:
        """Gets `BeautifulSoup` instance for specific page."""
        async with AsyncClient() as client:
            response = await client.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def _get_next_page_link(self, soup: BeautifulSoup):
        """Founds a link for a next page with a beasts."""

        def get_next_page_tag(tag: Tag) -> bool:
            """Founds a tag with a link for a next page with a beasts."""
            return all(
                [
                    tag.name == 'a',
                    tag.get('title') == 'Категория:Животные по алфавиту',
                    tag.text == 'Следующая страница',
                ]
            )

        next_page_tag = soup.find(get_next_page_tag)
        next_page_url = self.URL_BASE + next_page_tag['href']
        return next_page_url

    def _write_to_csv(self) -> None:
        """Write data to csv file."""
        with open(self.result_file_name, 'w', encoding='utf-8', newline='') as csvfile:
            beasts_writer = csv.writer(csvfile, delimiter=',',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for char, count in self.beasts_dict.items():
                beasts_writer.writerow([char, count])


if __name__ == '__main__':
    counter = BeastCounter()
    asyncio.run(counter.run_script())
