import os
import string
from asyncio import TaskGroup
from collections import namedtuple
from urllib.parse import quote

from httpx import AsyncClient
from bs4 import BeautifulSoup

from .errors import WrongSymbolInLetters

letter_and_link = namedtuple('letter_and_link', 'letter link')
RUSSIAN_LETTERS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENGLISH_LETTERS = string.ascii_uppercase
ALL_LETTERS = ENGLISH_LETTERS + RUSSIAN_LETTERS


class WikiAnimalsScraper(AsyncClient):
    """
    Данный класс является асинхронным скрапером животных с российской википедии.
    Его основные методы **scrape_animals_count** и **save_data** позволяют собирать количество
    всех видов животных и записывать их в csv-файл в алфавитном порядке.

    **Attributes**:
        *letters*: строка состоящая из букв верхнего или нижнего регистра(кириллица или латиница)
    Пример использования:

        async def main():
            scraper = WikiAnimalsScraper()\n
            await scraper.scrape_animals_count()\n
            print(scraper.animals_count) #{А: 10, Б:5...}\n
            scraper.save_data()
    """
    main_page_url: str
    letters: set
    animals_amount: dict

    def __init__(self, letters: str = RUSSIAN_LETTERS) -> None:
        super().__init__()
        self.main_page_url = ("https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80"
                              "%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0"
                              "%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&")
        self.letters = set(letters.upper())
        self.animals_amount = {letter: 0 for letter in self.letters}

    def _get_start_urls(self) -> tuple[letter_and_link]:
        return tuple(letter_and_link(letter=letter, link=f"{self.main_page_url}from={quote(letter)}")
                     for letter in self.letters)

    async def _scrape_from_page(self, letter_n_link: letter_and_link) -> None:
        # получаем ответ от сервера вики с информацией о видах
        response = await self.get(letter_n_link.link)
        content = response.text

        # инициализируем суп для удобного поиска по элементам страницы
        soup = BeautifulSoup(content, 'html.parser')

        # находим элемент с нужной информацией
        mw_pages = soup.find("div", {"id": "mw-pages"})
        mw_category_group = mw_pages.find('div', class_='mw-category-group'
                                          )
        # сверяем букву в списке с буквой, для которой ищем виды
        # это нужно, т.к. если закинуть Ъ, Ь, Ы, то вики кинет страницу с другой буквой
        letter = mw_category_group.find('h3').text
        if letter != letter_n_link.letter:
            return

        # ищем все элементы типа li и их количество добавляем к словарю по букве
        ul = mw_category_group.find('ul')
        links = ul.find_all('li')
        self.animals_amount[letter] += len(links)

        # если ссылок было меньше 200(за одну страницу вики выдает максимум 200 на нужную букву)
        # то таск завершается
        if len(links) < 200:
            return

        # если нет, то скрапим ссылку на следующую страницу
        next_page = mw_pages.find('a', string="Следующая страница")
        next_page_conditions = next_page.attrs.get('href')
        # к стартовой странице добавляем полученную ссылку и снова вызываем функцию с новым урлом
        next_page_url = self.main_page_url + ''.join(next_page_conditions)
        await self._scrape_from_page(letter_and_link(letter=letter, link=next_page_url))

    async def scrape_animals_count(self) -> dict[str, int]:
        """
        Данный метод просчитывает количество всех видов по буквам,
        записывает их в переменную *animals_count* и возвращает её
        """
        # получаем кортеж namedtuple'ов вида (letter, link)
        letters_n_links = self._get_start_urls()

        # инициализируем таскгруппу в асинк контекст-менеджере
        async with TaskGroup() as tg:

            # проходимся по кортежу со ссылками и именами и кидаем таскгруппе
            # задачи для скрапинга количества видов с определенного урл по определенной букве
            for lnl in letters_n_links:
                #Проверяем на наличие символа в кириллице и латинице
                if lnl.letter not in ALL_LETTERS:
                    raise WrongSymbolInLetters(lnl.letter)
                tg.create_task(self._scrape_from_page(lnl))

        return self.animals_amount

    async def save_data(self) -> str:
        """
        Данный метод записывает текущие значения из словаря *animals_count*
        в файл *beasts.csv*. Возвращает путь к файлу.\n
        Файл имеет вид:\n
        А,1000\n
        Б,100\n
        В,500\n
        ...

        """
        # создаем или открываем файл и записываем из словаря ключ и значение через запятую
        with open("../beasts.csv", mode='w', encoding='utf-8') as csv_file:
            for letter, count in self.animals_amount.items():
                csv_file.write(f"{letter},{count}\n")
            file_path = csv_file.name
        cur_path = os.getcwd()
        return os.path.join(cur_path, file_path)
