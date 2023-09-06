import requests
from bs4 import BeautifulSoup
from collections import *

URL = 'https://ru.wikipedia.org'
URL_BEASTS = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'


def wiki_parse(url):
    """ФУНКЦИЯ ПАРСЕРА"""
    count_beasts = Counter()  # словарь где ключ: (буква), а значение: (количество животных)

    while url:
        request = requests.get(url)  # получаем страницу
        data = request.text  # получаем ее шаблон

        bs = BeautifulSoup(data, 'html.parser')
        content_div = bs.find('div', class_="mw-category-columns")  # находим DIV с животными

        for li in content_div('li'):  # бежим по всем буквам, пока не закончатся
            letter = li.a.text[0]
            count_beasts[letter] += 1  # заносим в переменную. Вид в переменной: "А": 3228
            print(letter, count_beasts)

            next_page = bs.find('a', string="Следующая страница")  # находим элемент след стр, для поисква ее пути
            if not next_page:
                return file_create(count_beasts)  # если нет, то возращаем переменную нашу
            url = URL + next_page.get('href')  # переходим на след стр

    return file_create(count_beasts)


def file_create(count_beasts):
    """ФУНКЦИЯ ЗАПИСИ В ФАЙЛ"""
    with open('beasts.csv', 'w', encoding='UTF-8') as bst:
        for letter, count in sorted(count_beasts.items(), key=lambda x: (x[0].isascii(), x[0])):  # сортировка ASCII
            bst.write(f'{letter}, {count}\n')


if __name__ == "__main__":
    wiki_parse(URL_BEASTS)