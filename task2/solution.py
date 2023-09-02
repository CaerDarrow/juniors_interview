import csv
import requests
from bs4 import BeautifulSoup


class WikiAnimalsParser:
    __slots__ = ("filepath", "pages_limit", "data")

    start_url = "/wiki/Категория:Животные_по_алфавиту"
    domain_url = "https://ru.wikipedia.org"

    def __init__(self, filepath: str, pages_limit: int = 10000):
        self.pages_limit = pages_limit
        self.filepath = filepath
        self.data: [str, int] = {}

    def parse(self):
        current_page = 1
        current_url = self.domain_url + self.start_url
        while current_page < self.pages_limit:
            response = requests.get(current_url)
            if not response:
                raise ValueError(f"Response is not OK: {response}")
            soup = BeautifulSoup(response.content, "lxml")
            self._parse_animals(soup)
            pref_url, next_url = self._get_last_next_links(soup)
            print(self.data)
            current_url = self.domain_url + next_url

    def _parse_animals(self, soup: BeautifulSoup) -> None:
        columns_div = soup.find("div", {"class": "mw-category mw-category-columns"})
        for li_element in columns_div.find_all("li"):
            text = li_element.text.strip()
            letter = text[0].upper()
            if letter not in self.data:
                self.data[letter] = 1
            else:
                self.data[letter] += 1

    def _get_last_next_links(self, soup: BeautifulSoup) -> tuple[str, str]:
        link_tags = soup.find("div", {"id": "mw-pages"}).find_all("a", recursive=False)
        return tuple((link_tag['href'] for link_tag in link_tags[:2]))  # type: ignore


if __name__ == '__main__':
    parser = WikiAnimalsParser("animals.csv")
    parser.parse()
