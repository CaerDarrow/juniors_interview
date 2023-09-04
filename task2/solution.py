import csv
from collections import defaultdict

import requests

BASE_URL = 'https://ru.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'cmtitle': 'Категория: Животные по алфавиту',
    'cmprop': 'title',
    'cmlimit': 'max',
    'cmnamespace': 0,  # Указывает что нужно получать столько статьи
}


def get_pages(data):
    query = data.get('query', None)
    if not query:
        raise KeyError("query key don't exists in data")
    categories = query.get('categorymembers', None)
    if not categories:
        raise KeyError("categorymembers key don't exists in data")

    return categories


def get_beasts_name() -> tuple[dict, int]:
    result = defaultdict(int)
    beasts_count = 0

    while True:
        response = requests.get(BASE_URL, params)
        if response.status_code != 200:
            raise ValueError()

        data = response.json()
        beasts_name = get_pages(data)
        beasts_count += len(beasts_name)

        for category in beasts_name:
            title = category.get('title', None)
            print('Название животного:', title)
            if title:
                result[title[0].upper()] += 1

        # get next data part
        if data.get('continue', None):
            params['cmcontinue'] = data['continue']['cmcontinue']
        else:
            break

    return result, beasts_count


def write_to_file(animals):
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for animal, quantity in animals.items():
            writer.writerow([animal, quantity])


if __name__ == '__main__':
    beasts, count = get_beasts_name()
    print('Общее количество животных', count)
    print('Общее количество животных по буквам', beasts)
    write_to_file(beasts)
