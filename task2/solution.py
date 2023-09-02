import csv
import requests
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
BASE_URL = "https://ru.wikipedia.org"
FIRST_URL = "/wiki/Категория:Животные_по_алфавиту"


def pars_data(url):
    data = {}
    flag = True
    while flag:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quote = soup.find_all("div", {"class": "mw-category-group"})
        print(quote)
        for item in quote[2:]:
            letter = item.find_all("h3")[0].text
            if letter.isascii():
                flag = False
                break
            print(f"Смотрим животных на букву : {letter}")
            data[letter] = data.get(letter, 0) + len(
                item.find_all("ul")[0].find_all("li")
            )
        url = (
            "https://ru.m.wikipedia.org"
            + soup.find_all("a", {"title": "Категория:Животные по алфавиту"})[-1][
                "href"
            ]
        )
    return data


def get_page(url: str) -> BeautifulSoup:
    resp = requests.get(url).content
    soup = BeautifulSoup(resp, "lxml")
    return soup


def get_animals(soup: BeautifulSoup) -> list[str]:
    columns = soup.find_all("div", attrs={"class": "mw-category mw-category-columns"})
    links = [animal.findAll("a") for animal in columns][0]
    animals = [animal.get_text() for animal in links]
    return animals


def get_next_link(soup: BeautifulSoup) -> str:
    link = soup.find("a", string="Следующая страница")
    return link.get("href")


def save_data(filename: str, data: dict) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, value])


def parse(base_url, start_url) -> None:
    data = {}
    base = base_url
    next_url = start_url
    while True:
        page = get_page(base + next_url)
        animals = get_animals(page)
        for animal in animals:
            if animal[0].upper() in data.keys():
                data[animal[0].upper()] += 1
            else:
                data[animal[0].upper()] = 1
                print(f"Letter {animal[0]}")
        try:
            next_url = get_next_link(page)
        except Exception as e:
            break
    save_data("beasts.csv", data)


if __name__ == "__main__":
    parse(BASE_URL, FIRST_URL)
