import csv
import requests
from bs4 import BeautifulSoup


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
          }

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

data = {}
flag = True
while flag:
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    find = soup.find_all("div", {"class": "mw-category-group"})
    for item in find[2:]:
        tag = item.find_all("h3")[0].text
        if tag.isascii():
            flag = False
            break
        data[tag] = data.get(tag, 0) + len(
            item.find_all("ul")[0].find_all("li")
        )
    url = (
        "https://ru.m.wikipedia.org"
        + soup.find_all("a", {"title": "Категория:Животные по алфавиту"})[-1]["href"]
    )


req = requests.get(url, headers=headers).content
soup = BeautifulSoup(req, "lxml")
columns = soup.find_all("div", attrs={"class": "mw-category mw-category-columns"})

link = soup.find("a", string="Следующая страница")

with open("beasts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for key, value in data.items():
        writer.writerow([key, value])
