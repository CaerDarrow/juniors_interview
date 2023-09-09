import requests
from bs4 import BeautifulSoup
import csv


def get_all_links():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    hrefs = []
    table = soup.find('div', attrs={'class': 'mw-parser-output'})
    links = table.findAll('a')
    for link in links:
        if link['href'].startswith('https'):
            hrefs.append(link['href'])
    return hrefs


def get_animals(link: str):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('div', attrs={'class': 'mw-category mw-category-columns'})
    h3 = div.find('h3')
    lis = [x.text for x in div.findAll('li')]
    lis = list(filter(lambda x: x[0] == h3.text, lis))
    return h3.text.upper(), lis


def write_to_csv(animal_count):
    with open("animal.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
        # Записываем заголовок файла CSV
        writer.writerow(["Буква", "Количество"])

        # Записываем данные в файл CSV
        for letter in animal_count:
            writer.writerow([letter, len(animal_count[letter])])


animal_links = get_all_links()
result = {}
# print(get_animals(animal_links[0]))
for link in animal_links:
    letter, animals = get_animals(link)
    if letter in result:
        result[letter] = result[letter].union(animals)
    else:
        result[letter] = set()
    # print(result)
write_to_csv(result)
print("Данные успешно записаны в файл animals.csv.")
