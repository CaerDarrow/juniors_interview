import csv

import requests
import urllib.parse

RUS_URL = 'Категория:Животные_по_алфавиту'


def get_list(result, animals_list: list) -> list:
    for item in result['query']['categorymembers']:
        animals_list.append(item.get('title'))

    return animals_list


def get_wiki():
    url_encode = urllib.parse.quote(RUS_URL)
    url = ('https://ru.wikipedia.org/w/'
           'api.php?action=query'
           '&format=json'
           '&cmlimit=max'
           '&list=categorymembers'
           f'&cmtitle={url_encode}'
           '&cmcontinue=')

    animals_list = []
    animals_dict = {}
    next_page = ''

    while True:
        result = requests.get(url + next_page).json()
        animals_list = get_list(result, animals_list)
        try:
            next_page = result['continue']['cmcontinue']
        except KeyError:
            break

    animals_list = list(set(animals_list))

    for item in animals_list:
        first_letter = item[0].upper()
        if item[0] in animals_dict.keys():
            animals_dict[first_letter] += 1
        else:
            animals_dict[first_letter] = 1

    with open("beats.csv", "w") as file:
        writer = csv.writer(file)
        for row in animals_dict.items():
            writer.writerow(row)


if __name__ == '__main__':
    get_wiki()
