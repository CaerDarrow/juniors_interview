""" Решение задачи 2. """
import asyncio
import re
import requests
import copy
import csv


async def request(url: str, params: dict[str], sleep_time: float = 0.001) -> str:
    """ HTTP-запрос.

    :param url: Адрес.
    :param params: Параметры запроса в адресе.
    :param sleep_time: Время паузы для asincio
    :return: Ответ на запрос.
    """
    result = requests.get(url, params)
    return result.text


async def get_animals_count(answer: str, simbol: str, sleep_time: float = 0.001) -> int:
    """ Получить количество животных на странице.

    :param answer: Ответ сервера на HTTP-запрос.
    :param simbol: Буква, для которой ведётся сбор информации.
    :param sleep_time: Время паузы для asincio
    :return: Количество животных, выявленых в answer.
    """
    animal_pattern: re.Pattern = re.compile("<li><a\shref=\"/wiki/[^:]+?\"\stitle=\".+?\">{}.+?</a></li>".format(simbol))
    animals_blocks: list = re.findall(animal_pattern, answer)

    await asyncio.sleep(sleep_time)

    return len(animals_blocks)


async def get_url_to_next_page(answer: str, sleep_time: float = 0.001) -> str:
    """ Получить ссылку на следующую страницу.

    :param answer:  Ответ сервера на HTTP-запрос.
    :param sleep_time: Время паузы для asincio
    :return: Ссылка на следующую страницу. Если '', значит перехода не следующую страницу нет.
    """
    url_pattern: re.Pattern = re.compile("<a\shref=\"([^><]+)\"\stitle=\"Категория:Животные по алфавиту\">Следующая\sстраница</a>")
    group = re.search(url_pattern, answer)

    if group is None:
        # Если поиск не дал результатов
        return ''
    url: str = "https://ru.wikipedia.org" + group.group(1)
    # В извлечённой из html ссылке присутствует '&amp;'. HTTP запрос в этом случае будет возвращать не ту страницу.
    # Поэтому, произведена замена.
    url = re.sub('&amp;','&', url)
    await asyncio.sleep(sleep_time)
    return url


async def worker(url: str, params: dict, simbol: str, sleep_time: float = 0.001) -> int:
    """ Корутина, обрабатываемая параллельно.

    :param url: url-адрес
    :param params: Параметры http-запроса.
    :param simbol: Буква, для которой добывается информация (количество животных, название которых начинается на simbol)
    :param sleep_time: Время паузы для asincio
    :return: Количество обнаруженных животных на букву simbol
    """
    answer: str = await request(url, params, sleep_time)
    animals: int = await get_animals_count(answer, simbol, sleep_time)
    next_url: str = await get_url_to_next_page(answer, sleep_time)

    animals_count: int = 0
    if next_url != '':
        # Если есть переход на следующую страницу.
        if animals > 0:
            # Если на текущей странице ещё есть животные, то, предполагаем, что на следующей они тоже есть.
            animals_count = await worker(next_url, {}, simbol, sleep_time)

    return animals + animals_count


def write_csv(data: list[tuple[str, int]]) -> None:
    """ Запись csv файла.

    :param data: список кортежей вида [('A', 50)('Б', 13)]
    """
    with open('./beasts.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator='\r')
        csv_writer.writerows(data)


async def solution(sleep_time: float = 0.001) -> None:
    """

    :param sleep_time: Время паузы для asincio
    """
    url: str = "https://ru.wikipedia.org/w/index.php"
    params = {'title': 'Категория:Животные_по_алфавиту', 'from': 'A'}

    # Создание списка с буквами русского и латинского алфавитов.
    alphabet: list[str] = [chr(value) for value in range(ord('А'), ord('Я') + 1)]
    alphabet.append('Ё')
    # Латинский алфавит
    # alphabet.extend([chr(value) for value in range(ord('A'), ord('Z') + 1)])

    tasks: list = [None for i in range(len(alphabet))]

    for i, simbol in enumerate(alphabet):
        # Перебор алфавита и запуск корутин

        p_copy = copy.deepcopy(params)
        p_copy['from'] = simbol

        print("Сбор информации по букве '{}' запущен.".format(simbol))
        # Запуск задач.
        tasks[i] = asyncio.create_task(worker(url, p_copy, simbol, sleep_time), name=simbol)

        await asyncio.sleep(sleep_time)

    # Количество животных с разбивкой по буквам алфавита: [('A', 50)('Б', 13)]
    animals_count: list[tuple] = []
    # Список работающих задач
    runing_tasks: list = []

    while len(tasks) > 0:
        # Пока есть работающие задачи.

        for i, task in enumerate(tasks):
            # Переборка задач
            if task is not None:
                if not task.done():
                    # Если задача ещё не завершена
                    # Переносим её в список работающих задач.
                    runing_tasks.append(task)
                else:
                    # Если задача завершена
                    try:
                        # Попытка получить результат работы задачи.
                        animals_count.append(tuple([task.get_name(), task.result()]))
                        # print("Сбор информации по букве '{}' завершён.".format(task.get_name()))
                    except asyncio.CancelledError:
                        # Задача была отменена
                        pass
                    except Exception:
                        # Задача завершилась ошибкой.
                        exception = task.exception()

            await asyncio.sleep(sleep_time)

        # "Обновляем" обрабатываемый список задач.
        tasks, runing_tasks = runing_tasks, []

    print("Сбор информации по всем буквам русского алфавита завершён.")
    # Сортировка результатов в алфавитном порядке.
    animals_count = sorted(animals_count, key=lambda animals_count: animals_count[0])
    # Вставка Ё в нужное место.
    yo: tuple = animals_count.pop(0)
    animals_count.insert(6, yo)

    # Вывод результатов в файл.
    write_csv(animals_count)


if __name__ == '__main__':
    asyncio.run(solution(0.0001))