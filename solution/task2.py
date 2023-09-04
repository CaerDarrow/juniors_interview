import csv
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

'''Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список 
всех животных (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в 
формате beasts.csv количество животных на каждую букву алфавита. Содержимое результирующего файла:
А,642
Б,412
В,...'''


url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

req = requests.get(url).text

f = 1
result = defaultdict(int)
while f:
    soup = BeautifulSoup(req, 'lxml')

    block = soup.find('div', class_='mw-category mw-category-columns')
    category_letter = block.find('div', class_='mw-category-group')
    category = category_letter.find_next('h3').text
    animal_names = block.find_all('li')

    animals_names = [animal.text for animal in animal_names]
    
    names,names_dict = sum([1 for name in animals_names if name.startswith(category)]),{}
    names_dict.update({category: names})

    order = {}
    for key in names_dict:
        try:
            order[key] += int(names_dict[key])
        except:
            order[key] = int(names_dict[key])   
    
    for key, value in order.items():
        result[key] += int(value)
        print(key,value)
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            req = requests.get(url).text
            break # нужен для правильной работы else       
    else:
        f = 0
        break # прерывает цикл while

all_animals = dict(result)
with open("beasts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Буква","Колличество"])
    for animal in all_animals:
        writer.writerow([animal,all_animals[animal]])