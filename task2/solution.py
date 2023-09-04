import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = 'https://ru.wikipedia.org'
START_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
STOP_LETTER = 'A'


def fetch_animal_data(url):
    """
    Получает и парсит данные о животных с данной Wikipedia URL.
    Возвращает:
    - Словарь с подсчетом животных по буквам.
    - URL следующей страницы.
    """
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    animal_groups = soup.find_all('div', class_='mw-category-group')[2:]
    letter_counts = {}

    for group in animal_groups:
        letter = group.find('h3').text
        if letter == STOP_LETTER:
            return letter_counts, None
        entries = group.find_all('li')
        letter_counts[letter] = len(entries)

    next_page_anchor = soup.find('a', text="Следующая страница")
    next_page_url = BASE_URL + next_page_anchor['href'] if next_page_anchor else None

    return letter_counts, next_page_url


def main():
    total_counts = {}
    current_url = START_URL

    start_time = time.time()
    while current_url:
        new_counts, current_url = fetch_animal_data(current_url)
        for letter, count in new_counts.items():
            total_counts[letter] = total_counts.get(letter, 0) + count

    end_time = time.time()
    print(f"Program executed in {end_time - start_time:.2f} seconds")

    with open('beasts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for letter, count in sorted(total_counts.items()):
            writer.writerow([letter, count])


if __name__ == '__main__':
    main()
