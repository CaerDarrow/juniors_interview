import os
import re
import requests
from bs4 import BeautifulSoup

from solution import START_URL


def test_connection():
    """Тест соединения"""
    assert requests.get(START_URL).status_code == 200


def test_isfile():
    """Тест наличия файла"""
    assert os.path.isfile('./task2/beasts.csv') is True


def test_content():
    """Тест соответствия первой строки"""
    with open(file='./task2/beasts.csv',
              mode='r',
              encoding='UTF-8') as file:
        line = file.readline().splitlines()
        assert line[0] == 'А,1226'


def test_count_alph():
    """Тест соответствия данных о количестве статей со страницы википедии и
    полученных данных"""
    sum_alph = 0

    with requests.Session() as session:
        content = session.get(START_URL).content
        soup = BeautifulSoup(content, 'lxml')
        count_str = soup.findAll(string=re.compile("Показано 200 страниц из"))
        count_w = re.findall('[0-9]{5}', count_str[0].replace('\xa0', ''))[0]

    with open(file='./task2/beasts.csv',
              mode='r',
              encoding='UTF-8') as file:
        for line in file.readlines():
            sum_alph += int(line.split(',')[1])
    assert sum_alph == int(count_w)
