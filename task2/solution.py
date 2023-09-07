import os

BEAST_LIST_FILE_PATH = './list_of_beasts.csv'
RESULT_FILE_PATH = './beasts.csv'


def count(file_name):
    beast_counter = {}

    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            src = f.read()
            src = src.strip().split('\n')

        for beast in src:
            first_letter = beast.strip()[0].upper()
            if first_letter in beast_counter:
                beast_counter[first_letter] += 1
            else:
                beast_counter[first_letter] = 1

    except Exception as e:
        return f'Ошибка прочтения файла\n Exception: {e}\n {FileNotFoundError}'

    file_name = RESULT_FILE_PATH

    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write('\n'.join([f"{letter},{number}" for letter, number in beast_counter.items()]))


""" Для решения задачи я выбрала библтотеку Scrapy т.к. она бысрее
    чем, скажем, BeautifulSoup4 или Selenium из-за малого расхода памяти и
    оптимизации "под капотом".
    Я не стала сразу записывать количество животных и букву через цикл
    т.к. это занимало больше времени и свело на нет преимущества Scrapy в скорости.
    Поэтому оптимальнее было сначала записать список всех животных в отдельный файл,
    а затем отдельно сделать подсчет.
"""


def main():
    os.system('scrapy crawl beasts')
    count(BEAST_LIST_FILE_PATH)


if __name__ == '__main__':
    main()
