import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def parse_last():
    d = {}
    URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    while True:
        res = get_html(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes_link = soup.find_all('a', text='Следующая страница')
        quotes_words = soup.find_all('div', class_='mw-category-group')
        for i in quotes_words[2:]:
            list_cut = i.text.split('\n')
            if list_cut[0] in d:
                d[list_cut[0]] += len(list_cut) - 1
            else:
                if len(d) > 28:
                    return d, URL
                d[list_cut[0]] = len(list_cut) - 1
        URL = 'https://ru.wikipedia.org/' + quotes_link[1].get('href')


if __name__ == '__main__':
    res, fin = parse_last()
    print(f'{res} Finish {fin}')
    with open('res.csv', 'w', newline='') as csv_f:
        write = csv.writer(csv_f)
        for i in res.items():
            write.writerow(i)
