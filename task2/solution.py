from bs4 import BeautifulSoup
import requests
import csv

START_URL = "https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А"
DOMEN = "https://ru.wikipedia.org"
OUTPUT_CSV_NAME = "output.csv"
DICT = {}


def writeCsv():
    with open(OUTPUT_CSV_NAME, 'w', newline='', encoding="utf-8") as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        print(DICT)
        wr.writerows(DICT.items())


def parseWikiPage(url: str):
    page_source = requests.get(url=url).text
    soupe = BeautifulSoup(page_source, "lxml")
    value_columns = soupe.find("div", class_="mw-category mw-category-columns")
    value_groups = value_columns.findAll("div", class_="mw-category-group")
    for category in value_groups:
        char = category.find("h3").text
        if char == "A":
            return
        try:
            DICT[char] += 0
        except:
            DICT[char] = 0
        DICT[char] += len(category.find_all("li"))
    next_url_path = soupe.find("a", string="Следующая страница")["href"]
    parseWikiPage(DOMEN + next_url_path)


def test1():
    try:
        with open(OUTPUT_CSV_NAME, newline='', encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile)
            if len(list(spamreader)) == 29:
                return True
    except:
        pass
    return False


def test2():
    try:
        with open(OUTPUT_CSV_NAME, newline='', encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if len(row) != 2:
                    return False
            return True
    except:
        pass
    return False


def tests():
    if not test1():
        print("Test1 - Fail")
    if not test2():
        print("Test2 - Fail")


def main():
    parseWikiPage(START_URL)
    writeCsv()
    tests()


if __name__ == "__main__":
    main()
