import requests
from bs4 import BeautifulSoup
import csv


def parser(url):

    value_for_return = 0

    animal_count = {}

    while True:

        try:
            response = requests.get(url)
        except Exception:
            value_for_return = 1
            break

        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        category_groups = soup.find_all(class_="mw-category-group")
        next_page_link = soup.find("a", text="Следующая страница")
        try:
            next_page_ref = next_page_link.get('href')
            url = f'https://ru.wikipedia.org/{next_page_ref}'
        except Exception:
            break

        for category_group in category_groups:

            if 'Знаменитые животные по алфавиту' in category_group.get_text() or 'Породы собак по алфавиту' in category_group.get_text():
                continue
            
            letter = category_group.get_text()[0]
            
            animals = category_group.find_all("a")
            
            if letter in animal_count:
                animal_count[letter] = animal_count[letter] + len(animals)
            else:
                animal_count[letter] = len(animals)
            print(animal_count)


    if value_for_return == 0:
        with open("beasts.csv", "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Буква", "Количество животных"])
            for letter, count in animal_count.items():
                csv_writer.writerow([letter, count])
        return value_for_return
    else:
        return value_for_return