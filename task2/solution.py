import requests
from bs4 import BeautifulSoup
import csv


def beasts_parser(headers):
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    session = requests.Session()
    beasts_list = []
    while True:
        resp = session.get(url, headers=headers)
        status_code = resp.status_code
        if status_code!=200:
            return None
        dom = BeautifulSoup(resp.content, 'html.parser')
        big_letters = dom.find_all('td', attrs={'style':'font-weight:bold'})
        for i in big_letters:
            beast_link = i.find('a')['href']
            beast_name = i.find('a').text
            beast_finder = session.get(beast_link, headers=headers)
            letter_dom = BeautifulSoup(beast_finder.content, 'html.parser')
            beast_digit = 0
            digit_checker=True
            while digit_checker==True:
                all_beasts_finder = letter_dom.find('div', attrs={'class':'mw-category mw-category-columns'}).find('div', attrs={'class':'mw-category-group'}).find('ul')
                button_next = letter_dom.find('a', text='Следующая страница')['href']
                beasts_count=0
                for j in all_beasts_finder.find_all('li'):
                    beasts_count+=1
                beast_digit+=beasts_count
                if beasts_count<200:
                    digit_checker=False
                    beasts_list.append([beast_name,beast_digit])
                if button_next:
                    full_adress='https://ru.wikipedia.org'+button_next
                    beast_finder = session.get(full_adress, headers=headers)
                    letter_dom = BeautifulSoup(beast_finder.content, 'html.parser')
                else:
                    digit_checker=False
                    beasts_list.append([beast_name,beast_digit])
                      
        break
    return beasts_list


def csv_writer(file, b_list):
    try:
        with open(file, mode='w') as f:
            file_writer=csv.writer(f,delimiter=',', lineterminator='\r')
            for i in b_list:
                file_writer.writerow([i[0], i[1]])
        return True
    except FileNotFoundError: 
        return 'File is not found'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'
}
writer = csv_writer('beasts.csv', beasts_parser(headers))
