import sys
import tracemalloc

import requests
import csv

from bs4 import BeautifulSoup

tracemalloc.start()


class WikiAnimalsParsing:
    letter: str = ""
    alphabet: dict = {}
    area_list: list[str] = []
    area_set: set[str] = set()
    exit_parser: bool = False
    url_from: str = f"https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from="
    url: str = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    ALPHABET: list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
                      'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                      'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z']

    def parser_launch(self, start_letter: str = None, stop_letter: str = None) -> dict:
        """
        Определяет зону действия парсера и обновляет значения
        :param start_letter: Буква с которой парсер начнет
        :param stop_letter: Буква на которой парсер остановится
        :return: Возвращает словарь с количеством животных для каждой буквы
        """
        self.letter: str = ""
        self.alphabet: dict = {}
        self.area_list: list[str] = []
        self.area_set: set[str] = set()
        self.exit_parser: bool = False
        self.url: str = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        index_start = self.ALPHABET.index(start_letter) if start_letter else None
        index_stop = self.ALPHABET.index(stop_letter) + 1 if stop_letter else None
        # Меняет местами стартовую и конечную буквы если нарушена последовательность
        if index_stop is not None and index_start is not None and index_stop <= index_start:
            self.area_list = self.ALPHABET[index_stop-1:index_start+1]
        else:
            self.area_list = self.ALPHABET[index_start:index_stop]
        if start_letter:
            self.url = f"{self.url_from}{self.area_list[0]}"
        self.area_set = set(self.area_list)
        self.wiki_animals_parsing()
        return self.alphabet

    def wiki_animals_parsing(self):
        """
        Цикличный парсинг страниц до условленного момента
        """
        while not self.exit_parser:
            contents = requests.get(self.url).text
            soup = BeautifulSoup(contents, 'html.parser')
            content_div = soup.find('div', attrs={'class': 'mw-category-columns'})
            next_url = soup.find('a', string='Следующая страница')
            del contents, soup
            self.walk_through_tags(content_div)
            del content_div
            if next_url is None:
                self.exit_parser = True
            if self.exit_parser:
                self.write_down()
                break
            self.url = "https://ru.wikipedia.org" + next_url.get('href')

    def walk_through_tags(self, content_div):
        """
        Проход по полученным тегам со страницы для подсчета результата
        :param content_div: принимает интересующую нас часть html разметки сайта
        """
        for raw in content_div.select('li, h3'):
            self.state_of_progress()
            if raw.name == 'h3':
                # Проверка на случай инъекций в заголовках.
                # Например когда русская "М" вдруг встречается в английской "Т"
                if self.letter != "" and self.ALPHABET.index(raw.text) < self.ALPHABET.index(self.letter):
                    self.letter = self.letter
                else:
                    self.letter = raw.text
                if self.letter not in self.area_set:
                    self.exit_parser = True
                    break
                else:
                    if not self.alphabet.get(self.letter):
                        self.alphabet.setdefault(self.letter, 0)
            elif raw.name == 'li':
                self.alphabet[self.letter] += 1

    def write_down(self):
        """
        Запись полученных значений в файл
        """
        with open("beasts.csv", 'w') as f:
            fieldnames = ['letter', 'quantity']
            for letter in self.area_list:
                if self.alphabet.get(letter):
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerow({'letter': letter, 'quantity': str(self.alphabet[letter])})
        sys.stdout.write("\r" + "Done!")

    def state_of_progress(self):
        """
        Вывод строки состояния:
            какая буква сейчас парсится
            язык буквы
            шкала прогресса
            текущее и пиковое значения затраченной памяти
        """
        if self.letter == "":
            self.letter = self.area_list[0]
        index = self.area_list.index(self.letter)
        done = int(100/len(self.area_list) * index)
        planned = 100 - done
        space = (3 - len(str(done))) * " "
        language = 'RU' if self.ALPHABET.index(self.letter) < 33 else 'EN'
        current = round(tracemalloc.get_traced_memory()[0]/1048576, 2)
        peak = round(tracemalloc.get_traced_memory()[1]/1048576, 2)
        sys.stdout.write(f"\rIn progress...[{self.letter}|{language}]{space}{done}% "
                         f"{'▓' * done}{'░' * planned} current:{current}Mb | peak:{peak}Mb")


W = WikiAnimalsParsing()

# W.parser_launch()


tracemalloc.stop()
