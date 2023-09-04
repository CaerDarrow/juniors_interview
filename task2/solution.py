from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from collections import defaultdict
import csv


driver = webdriver.Chrome()

driver.get(
    "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
)

animal_count = defaultdict(int)


while True:
    elements = driver.find_elements(
        By.CSS_SELECTOR, "#mw-pages .mw-category-group ul li a"
    )
    for element in elements:
        animal_count[element.text[0].upper()] += 1
    try:
        next_page_link = driver.find_element(By.LINK_TEXT, "Следующая страница")
    except NoSuchElementException:
        driver.quit()
        break
    else:
        next_page_link.click()

with open("task2/beasts.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    for key, value in animal_count.items():
        writer.writerow([key, value])
