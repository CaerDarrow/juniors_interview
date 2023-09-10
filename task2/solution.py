from bs4 import BeautifulSoup
import httpx
import sys


base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
ans_for_csv = dict()
is_english_names = False


def get_info_from_current_page(url: str) -> str:
    response = httpx.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    need_div = soup.find_all('div', class_='mw-category mw-category-columns')
    for elem_h in need_div[:1]:
        ul = elem_h.find_all('ul')
        for elem_ul in ul:
            a_tag = elem_ul.find_all('a')
            for elem_a in a_tag:
                animal = elem_a.get_text()
                if not is_english_names and animal[0] == 'A':
                    return ""
                words = animal.split()
                if len(words) == 1:
                    ans_for_csv[animal[0]] = ans_for_csv.get(animal[0], 0) + 1
                else:
                    ans_for_csv[words[-1][0].upper()] = ans_for_csv.get(words[-1][0].upper(), 0) + 1
    find_link_next_page = soup.find_all('div', id='mw-pages')
    a_tags = find_link_next_page[0].find_all('a')
    check_text = [a_tags[1].get_text(), a_tags[2].get_text()]
    if 'Следующая страница' not in check_text:
        return ""
    ret_link = "https://ru.wikipedia.org" + a_tags[-1].get('href')
    return ret_link


def get_all_pages_and_info(url):
    cur_link = url
    while cur_link:
        cur_link = get_info_from_current_page(cur_link)


"""
Если нужно получить в csv еще и латинские буквы, прописываем в параметры запуска программы флаг -eng
Пример запуска на Linux(из начальной директории репозитория):
python3 task2/solution.py -eng
"""
if __name__ == "__main__":
    if "-eng" in sys.argv:
        is_english_names = True
    get_all_pages_and_info(base_url)
    with open("beasts.csv", "a+") as csv_file:
        for key, value in sorted(ans_for_csv.keys()):
            str_csv = f"{key},{ans_for_csv[key]}\n"
            csv_file.write(str_csv)
