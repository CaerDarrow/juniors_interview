from requests import get
from bs4 import BeautifulSoup
from bs4.element import Tag
from threading import Thread
import csv

DICT_LETTERS = dict()
WIKI_ADR = "https://ru.wikipedia.org/"
 
def calc_animals_on_page(tag_ul: Tag, letter: str) -> bool: 
    for tag_li in tag_ul.find_all("li"):
        tag_a = tag_li.find("a")
        name_animal = tag_a.text
        if name_animal.lower()[0] != letter.lower():
            return False
        if name_animal[0] not in DICT_LETTERS.keys():
            DICT_LETTERS[name_animal[0]] = 1
        else:
            DICT_LETTERS[name_animal[0]] += 1
    return True

def calc_animals(letter: str, link: str):
    while True:
        response = get(link)
        root = BeautifulSoup(response.text, 'html.parser')
        tag_ul = root.find("div", id = "mw-pages").find("div", class_ = "mw-category-group").find("ul")
        if not calc_animals_on_page(tag_ul, letter):
            break
        tag_a = root.find("div", id = "mw-pages").find("a", string="Следующая страница")
        link = WIKI_ADR + tag_a["href"]

def main():
    link = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    response = get(link)
    root = BeautifulSoup(response.text, 'html.parser')
    row = root.find("table", class_ = "plainlinks").find_all("tr")[1]
    threads = []
    for tag_td in row.find_all("td"):
        tag_a = tag_td.find("a")
        letter = tag_a.text
        link = tag_a["href"]
        thread = Thread(target=calc_animals, args=(letter, link))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    sorted_tuple = sorted(DICT_LETTERS.items())
    with open("beasts.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(sorted_tuple)
        
main()