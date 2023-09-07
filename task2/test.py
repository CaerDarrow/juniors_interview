import csv
import unittest
from solution import WikiAnimalsScraper
from solution.errors import WrongSymbolInLetters


class TestWikiScraper(unittest.IsolatedAsyncioTestCase):

    async def test_save_data(self):
        scraper = WikiAnimalsScraper("АБВ")
        await scraper.scrape_animals_count()
        path = await scraper.save_data()
        with open(path, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                self.assertEqual(len(row), 2)

    async def test_animals_count_scrape_case1(self):
        scraper = WikiAnimalsScraper("АБВ")
        data = await scraper.scrape_animals_count()
        self.assertEqual(data, {'А': 1225, 'Б': 1686, 'В': 533})

    async def test_animals_count_scrape_case2(self):
        scraper = WikiAnimalsScraper("CDFGЮЯ")
        data = await scraper.scrape_animals_count()
        self.assertEqual(data, {'C': 2523, 'D': 1081, 'F': 209, 'G': 692, 'Ю': 138, 'Я': 211})

    async def test_animals_count_scrape_case3(self):
        scraper = WikiAnimalsScraper("атпнАППн")
        data = await scraper.scrape_animals_count()
        self.assertEqual(data, {'Н': 471, 'Т': 1013, 'А': 1225, 'П': 1801})

    async def test_animals_count_scrape_wronk_letter_error(self):
        scraper = WikiAnimalsScraper("АБВ/")
        try:
            await scraper.scrape_animals_count()
        except ExceptionGroup as eg:
            self.assertEqual(eg.exceptions[0].__class__, WrongSymbolInLetters)


if __name__ == "__main__":
    unittest.main()