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
        last_links = []
        current_url = self.domain_url + self.start_url
        while current_page < self.pages_limit:
            response = requests.get(current_url)
            if not response:
                raise ValueError(f"Response is not OK: {response}")
            soup = BeautifulSoup(response.content, "lxml")
            self._parse_animals(soup)
            links = self._get_last_next_links(soup)
            _, next_url = links
            if next_url in last_links:
                break
            if len(last_links) >= 8:
                last_links = links
            else:
                last_links.extend(links)
            current_url = self.domain_url + next_url
        self._save_to_file()

    def _parse_animals(self, soup: BeautifulSoup) -> None:
        columns_div = soup.find("div", {"class": "mw-category mw-category-columns"})
        for li_element in columns_div.find_all("li"):
            text = li_element.text.strip()
            letter = text[0].upper()
            if letter not in self.data:
                self.data[letter] = 1
            else:
                self.data[letter] += 1

    def _save_to_file(self):
        with open(self.filepath, "w")as file:
            dict_writer = csv.DictWriter(file, ["letter", "amount"])
            dict_writer.writerows({"letter": k, "amount": v} for k, v in self.data.items())

    def _get_last_next_links(self, soup: BeautifulSoup) -> list[str, str]:
        link_tags = soup.find("div", {"id": "mw-pages"}).find_all("a", recursive=False)
        return [link_tag['href'] for link_tag in link_tags[:2]]  # type: ignore


if __name__ == '__main__':
    parser = WikiAnimalsParser("beasts.csv")
    parser.parse()
