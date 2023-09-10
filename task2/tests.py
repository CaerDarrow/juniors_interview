import sys

from solution import get_all_pages_and_info, ans_for_csv, base_url, is_english_names
from bs4 import BeautifulSoup
import httpx


def get_current_articles_count(url):
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    find_info_about_pages = soup.find_all('div', id='mw-pages')[0].find_all('p')
    array_text = find_info_about_pages[0].get_text().split()
    total_pages = int(array_text[4]) * 1000 + int(array_text[5][:-1])
    return total_pages


"""
Здесь тест к задаче подойдет, на мой взгляд один - количество записанных нами страниц должно совпадать с общим
числом страниц в данной категории. Проверять какие-то буквы на равенство точному значению не совсем возможно -
зависит от того, как трактовать запись в словарь - например в "Асписовая гадюка" мы можем записать как А, так и Г.
Поскольку в условии написано, что анализ текста не нужно проводить, то будем брать первую букву названия животного, как
в категории по букве.
"""
if __name__ == "__main__":
    args = sys.argv
    if "-eng" in args:
        is_english_names = True
    get_all_pages_and_info(base_url)
    current_total_articles = get_current_articles_count(base_url)

    if is_english_names:
        assert current_total_articles == sum(ans_for_csv.values())
