import requests
from bs4 import BeautifulSoup
import csv


def fetch_animals():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    animals = []

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        div_mw_pages = soup.find("div", {"id": "mw-pages"})
        h2_element = div_mw_pages.find(
            "h2", string="Страницы в категории «Животные по алфавиту»"
        )
        if h2_element:
            div_mw_category_group = div_mw_pages.find(
                "div", {"class": "mw-category-group"}
            )
            count = -1
            for tag in div_mw_category_group.find_all():
                if tag.name == "h3":
                    letter = tag.text.strip()
                    count = -1
                if tag.find("a") is not None:
                    count += 1

            found_dict = None
            for animal_dict in animals:
                if letter in animal_dict:
                    found_dict = animal_dict
                    break

            if found_dict:
                found_dict[letter] += count
            else:
                animals.append({letter: count})

        next_page_link = soup.find("a", string="Следующая страница")
        print(animals)
        if next_page_link:
            url = "https://ru.wikipedia.org" + next_page_link["href"]
        else:
            break

    return animals


def save_to_csv(animals):
    with open("animals.csv", "w", newline="") as csvfile:
        fieldnames = ["letter", "count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for animal_dict in animals:
            for letter, count in animal_dict.items():
                writer.writerow({"letter": letter, "count": count})


animals = fetch_animals()
save_to_csv(animals)
