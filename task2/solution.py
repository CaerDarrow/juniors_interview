from __future__ import annotations
import csv
import requests
from bs4 import BeautifulSoup, Tag

URL = "https://ru.wikipedia.org"
URL_CATEGORY = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"


def get_html(url: str) -> str:
    with requests.get(url) as response:
        html = response.text
        return html


def get_next_page(page: Tag) -> str | None:
    next_page = page.find_all(name="a", title="Категория:Животные по алфавиту")[-1]
    link_next_page = next_page["href"] if next_page.text == "Следующая страница" else None
    return link_next_page


def parser(url: str) -> dict[str, int]:
    result = {}

    while True:
        html = get_html(url)
        soup = BeautifulSoup(markup=html, features="html.parser")
        page = soup.find(name="div", id="mw-pages")

        next_page = get_next_page(page)
        if next_page is None:
            break

        symbol_group = (page
                        .find(name="div", class_="mw-category-columns")
                        .find_all(name="div", class_="mw-category-group"))

        for item in symbol_group:
            symbol = item.h3.text
            count_animals = len(item.find_next(name="ul"))

            if symbol not in result:
                result[symbol] = 0
                print(f"Обрабатываются названия на букву - {symbol}")
            result[symbol] += count_animals

        url = f"{URL}{next_page}"

    return result


def write_to_file(obj: dict[str, int]) -> None:
    with open('beasts.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')

        for symbol, count in obj.items():
            writer.writerow([symbol, count])


if __name__ == '__main__':
    animals = parser(URL_CATEGORY)

    write_to_file(animals)
