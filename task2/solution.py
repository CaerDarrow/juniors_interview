import requests
import csv
from bs4 import BeautifulSoup


url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
responce = requests.get(url)
soup = BeautifulSoup(responce.content, 'lxml')

def get_animal_list(soup):
    animal_list = soup.find(
        'div', class_='mw-category mw-category-columns'
    ).find('div', class_='mw-category-group').find_all('li')
    return animal_list


def get_next_page_link(soup):
    next_link = soup.find("a", string="Следующая страница")
    if next_link:
        return f'https://ru.wikipedia.org{next_link["href"]}'
    return None


def write_to_csv(data):
    with open("beasts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for letter, count in data.items():
            writer.writerow([letter, count])


def run_parser(soup, responce):
    if responce.status_code == 200:
        counter = {}
        while True:

            for animal in get_animal_list(soup):
                first_letter = animal.text[0].upper()
                counter[first_letter] = counter.get(first_letter, 0) + 1

            next_page_link = get_next_page_link(soup)
            if next_page_link:
                responce = requests.get(next_page_link)
                soup = BeautifulSoup(responce.content, 'lxml')
            else:
                break

    write_to_csv(counter)
    

if __name__ == '__main__':
    run_parser(soup, responce)
