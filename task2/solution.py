'''
python3.9 ubuntu
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество животных на каждую букву алфавита. Содержимое результирующего файла:
А,642
Б,412
В,....
Примечание:
анализ текста производить не нужно, считается любая запись из категории (в ней может быть не только название, но и, например, род)
'''

import requests
import time
import random
import pandas as pd
from bs4 import BeautifulSoup




def fill_output_file(some_link):
    r = requests.get(some_link)
    print(r)
    with open('output.txt', 'w') as out:
        print(r.text, file=out)
        out.close()


def write_names(soup_file):
    cirillic = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    listik_nazvaniy = []
    class_with_names =soup_file.find(class_="mw-category mw-category-columns").find_all("a")
    with open('beasts_full.csv', 'a') as beasts_full:
        for i, item in enumerate(class_with_names):
            listik_nazvaniy.append(item.get("title"))
            if listik_nazvaniy[i][0] in cirillic:
                beasts_full.write(listik_nazvaniy[i]+', '+listik_nazvaniy[i][0]+'\n')
            else:
                beasts_full.close()
                return 'end_program'
    beasts_full.close()


def create_next_link(some_soup_file):
    initial_partial_link = some_soup_file.find(class_="mw-category-generated").find_all("a")
    partial_link = str(initial_partial_link[-1]).split()
    partial_link = str(partial_link[1]).split('"')
    partial_link = str(partial_link[1]).split("amp;")
    partial_link = str(partial_link[0]) + str(partial_link[1])
    next_page = 'https://ru.wikipedia.org' + partial_link
    return next_page


def update_bs_object(bs_object):
    input_file = open('output.txt', 'r')
    bs_object = BeautifulSoup(input_file, 'lxml')
    input_file.close()
    return bs_object


def parse_page(page_link, bs_object):
    time.sleep(random.randint(3, 7))
    fill_output_file(page_link)
    bs_object = update_bs_object(bs_object)
    state = write_names(bs_object)
    page_link = create_next_link(bs_object)
    return page_link, bs_object, state

def shape_final_csv():
    df = pd.read_csv('beasts_full.csv')
    df = df.groupby('letter_tag')['name'].count()
    df.to_csv('beasts.txt', header='')




initial_link = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

last_page = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%AF%D1%8E&subcatfrom=%D0%AF%D1%8E&pagefrom=%D0%AF%D1%8E#mw-pages'
state = 'continue'


fill_output_file(initial_link)

input_file = open('output.txt', 'r')
bs = BeautifulSoup(input_file, 'lxml')
input_file.close()

with open('beasts_full.csv', 'a') as beasts_full:
    print('name,letter_tag', file=beasts_full)
    beasts_full.close()
write_names(bs)

next_page = create_next_link(bs)

while state != 'end_program':
    next_page, bs, state = parse_page(next_page, bs)


shape_final_csv()
print('program finished')
