import requests
import csv


def get_animal_list():
    url = 'https://ru.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'cmtitle': 'Категория:Животные по алфавиту',
        'cmprop': 'title',
        'cmstartsortkeyprefix': '',
        'cmlimit': 500
    }

    animals = []

    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print('Не удалось получить данные с Википедии')
            return []

        data = response.json()
        if 'categorymembers' in data['query']:
            for item in data['query']['categorymembers']:
                if item['ns'] == 0:
                    animals.append(item['title'])
        else:
            break

        if 'continue' in data:
            params['cmcontinue'] = data['continue']['cmcontinue']
        else:
            break

    return animals


# Функция для счетчика животных по каждой букве алфавита и записи в файл
def count_animals(animals):
    counts = {}

    for animal in animals:
        first_letter = animal[0].upper()
        if first_letter not in counts:
            counts[first_letter] = 0
        counts[first_letter] += 1

    with open('fauna.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])


# Получаем список животных
animals = get_animal_list()
print(animals)  # Добавлен отладочный вывод
# Считаем животных по каждой букве алфавита и записываем в файл
count_animals(animals)
