# Вариант для ответа если учитывать названия на русском языке и латинском
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from collections import Counter,OrderedDict

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
page = requests.get(url)

def write_in_file(file_name,result):
    with open(file_name,'w',encoding="utf-8") as file:
        for key, value in result.items():
            file.write(f"{key},{value}\n")


def get_soup(page):
    soup = BeautifulSoup(page, 'html.parser')
    soup_el_body = soup.find('div', class_='mw-category mw-category-columns')
    soup_result_animals = soup_el_body.find_all("li")
    return soup_result_animals


def get_list_animals(animals):
    result_list = []
    for animal in animals:
        href_animal = animal.find('a')
        result_list.append(href_animal.text)
    return result_list


driver = webdriver.Firefox()
driver.get(url)

count = 0
result = []
page = page.text

while True:
    animals = get_soup(page)
    result.extend(get_list_animals(animals))
    try:
        element = driver.find_element(By.XPATH, '//*[text() = "Следующая страница"]')
    except NoSuchElementException:
        break
    element.click()
    page = driver.page_source

result_counter = Counter(s[0] for s in result)
result_sort = OrderedDict(sorted((dict(result_counter).items())))
write_in_file("beasts.csv",result_sort)
