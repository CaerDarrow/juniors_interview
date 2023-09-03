#!/usr/bin/env python

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from time import perf_counter


class WikiBeasts:
    TASK_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    TASK_PATH = './task2/'

    def __init__(self, driver):
        self.driver = driver

    def connect(self, link: str) -> None:
        self.driver.get(link)

    def get_beasts_count(self) -> None:
        beasts_count = {}
        self.connect(self.TASK_URL)

        while True:
            beasts_category = self.driver.find_element(By.CSS_SELECTOR, 'div.mw-category.mw-category-columns')
            beasts_list = beasts_category.find_elements(By.CSS_SELECTOR, '.mw-category-group')

            for beast_group in beasts_list:
                letter = beast_group.find_element(By.TAG_NAME, 'h3').text.strip()
                # stop the loop when the Russian alphabet is finished
                if letter == 'A':
                    return beasts_count

                count = len(beast_group.find_elements(By.TAG_NAME, 'li'))

                if beasts_count.get(letter):
                    beasts_count[letter] += count
                else:
                    beasts_count[letter] = count

            next_page = self.driver.find_element(By.LINK_TEXT, 'Следующая страница')
            if next_page:
                next_page.click()
            else:
                break
            
        return beasts_count

    def write_to_csv(self, beasts: dict) -> None:
        name = 'beasts.csv'
        final_path = f'{self.TASK_PATH}{name}'

        with open(final_path, mode='w+') as file:
            writer = csv.writer(file)
            writer.writerow(beasts.keys())
            writer.writerow(beasts.values())

    

if __name__ == '__main__':
    start = perf_counter()

    driver = webdriver.Chrome(service=Service(), options=webdriver.ChromeOptions())
    wb = WikiBeasts(driver=driver)

    beasts_count = wb.get_beasts_count()
    wb.write_to_csv(beasts=beasts_count)

    driver.quit()

    end = perf_counter() - start
    print(end, 's')

