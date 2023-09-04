import requests

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

def test_wiki():
    response = requests.get(url).status_code
    assert response == 200