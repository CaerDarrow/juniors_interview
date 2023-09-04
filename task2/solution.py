from bs4 import BeautifulSoup, ResultSet
from requests import get
from tqdm import trange
import csv


def count_animals_on_page(div_with_hrefs: ResultSet) -> dict:
    """Функция считает количество ссылок на животных на странице по первым буквам,
    на вход принимает объект beautiful soup"""
    letter = ""
    count = 0
    counts = {}
    for num, string in enumerate(div_with_hrefs):
        if num > 1:
            string = str(string)
            prev_chars = '____'
            for char in string:
                if prev_chars == '<li>':
                    count += 1
                if prev_chars == '<h3>':
                    if letter not in counts and letter != "":
                        counts.update({letter: count})
                        count = 0
                    letter = char
                prev_chars += char
                prev_chars = prev_chars[1:]
    counts.update({letter: count})
    return counts


def make_link_next_page(string_with_link_next_page: str) -> str:
    """Функция составляет и очищает ссылку для перехода парсера на следующую страницу"""
    link = 'https://ru.wikipedia.org'
    clean_link = ""
    reading_flag = 0
    for char in string_with_link_next_page:
        if char == ',':
            reading_flag = 1
        if reading_flag == 2:
            link += char
        if reading_flag == 3:
            break
        if char == '"' and reading_flag > 0:
            reading_flag += 1
    last_chars = ""
    for char in link:
        clean_link += char
        last_chars += char
        if len(last_chars) > 5:
            last_chars = last_chars[1:]
        if last_chars == "&amp;":
            clean_link = clean_link[:-4]
    return clean_link


def read_the_page(link: str) -> (dict, str, str):
    """Получает страницу по предложенной ссылке, возвращает словарь с количеством животных, ссылку на следующую
    страницу и информацию о количестве животных всего (для прогресс-бара)"""
    response = get(link)
    counts, link_next_page, total_num = {}, "", ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        string_with_total_num_data = soup.findAll('p')
        total_num = parse_total_num_of_animals(string_with_total_num_data)
        div_with_hrefs = soup.findAll('div', class_='mw-category-group')
        counts = count_animals_on_page(div_with_hrefs)
        string_with_link_next_page = str(soup.findAll('a', title='Категория:Животные по алфавиту'))
        link_next_page = make_link_next_page(string_with_link_next_page)
    return counts, link_next_page, total_num


def parse_total_num_of_animals(string_with_total_num_data: ResultSet) -> str:
    """Парсит число с общим количеством животных для прогресс-бара, на вход принимает объект Beautiful Soup"""
    total_num = ""
    activate_counter = 0
    prev_chars = "________"
    for char in str(string_with_total_num_data):
        if prev_chars == "Показано":
            activate_counter += 1
        if activate_counter > 0:
            activate_counter += 1
        if 17 < activate_counter < 24:
            total_num += char
        prev_chars += char
        prev_chars = prev_chars[1:]
    total_num = total_num.replace('\xa0','')
    return total_num


def write_csv_file(dictionary_with_letters_count: dict) -> None:
    """Запись итогового словаря в csv файл"""
    with open('beasts.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(dictionary_with_letters_count.items())


if __name__ == "__main__":
    """Основной поток. Дает первое вхождение и запускает цикл парсера, по результатам составляет общий словарь, 
    который записывается в файл"""
    first_enter_link = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    counts, link_next_page, total_num = read_the_page(first_enter_link)
    dictionary_with_letters_count = {}
    visited_links = set()
    with trange(int(total_num)) as progress:
        while link_next_page not in visited_links:
            visited_links.add(link_next_page)
            counts, link_next_page, total_nums = read_the_page(link_next_page)
            for letter, count in counts.items():
                count_in_dict = count
                if letter in dictionary_with_letters_count:
                    count_in_dict = dictionary_with_letters_count.get(letter)
                    count_in_dict += count
                dictionary_with_letters_count.update({letter: count_in_dict})
            progress.update(int(total_num)*1.01/200)
    write_csv_file(dictionary_with_letters_count)
    print('Файл beasts.csv готов')

