from bs4 import BeautifulSoup
from time import sleep
import requests
import csv


class State():
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.current_letter = letter_list[0]
        self.animals_dict = {}
        self.unic_animals = []

    def parse_letter(self):
        link = self.current_letter['href']
        letter = self.current_letter['text'][0]
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find('div', class_='mw-category mw-category-columns')
        elements = table.findAll('li')
        count = 0
        for i in elements:
            element = i.find('a')
            if (element['href'] not in self.unic_animals) and (element.text[0] == letter):
                    self.unic_animals.append(element['href'])
                    count += 1
        if self.animals_dict.get(letter):
            self.animals_dict[letter] += count
        else:
            self.animals_dict.setdefault(letter, count)
        
    def worker(self):
        self.letter_list = self.letter_list
        count = 0
        for i in self.letter_list:
            self.current_letter = i
            self.parse_letter()
            count += 1
        print(self.animals_dict)
        with open('beasts.csv', 'w', newline='') as csvfile:
            fieldnames = ['letter', 'count']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for i in self.animals_dict.keys():
                writer.writerow([i, self.animals_dict[i]])

    

url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90'

def get_pages(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find('tbody')
    pages = table.findAll('a', class_='external text')
    data = []
    for i in pages:
        if len(i.text) <= 2:
            data.append({'href': i['href'], 'text': i.text})
    return data


if __name__ == "__main__":
    s = State(get_pages(url))
    s.worker()
