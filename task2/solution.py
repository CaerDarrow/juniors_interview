""" Решение задачи 2. """
import asyncio
import re
import requests
import string
import urllib.parse
import copy


async def request(url: str, params: dict[str], sleep_time: float = 0.001) -> str:
    """ HTTP запрос. """
    result = requests.get(url, params)
    await asyncio.sleep(sleep_time)
    return result.text


async def get_animals_count(answer: str, simbol: str, sleep_time: float = 0.001) -> int:
    """ Получить количество животных на странице. """
    # next_simbol: str = 'В'
    # animal_pattern: re.Pattern = re.compile("<li><a\shref='/wiki/.+?\"\stitle=\".+?'>.+?</a></li>")
    animal_pattern: re.Pattern = re.compile("<li><a\shref=\"/wiki/[^:]+?\"\stitle=\".+?\">{}.+?</a></li>".format(simbol))
    # animal_pattern: re.Pattern = re.compile("href")
    animals_blocks: list = re.findall(animal_pattern, answer)
    # for animal in animals_blocks:
    #     print(animal)

    await asyncio.sleep(sleep_time)

    return len(animals_blocks)


async def get_url_to_next_page(answer: str, sleep_time: float = 0.001) -> str:
    """ Получить ссылку на следующую страницу. """
    # url_pattern: re.Pattern = re.compile("<a\shref=\".+?\"\stitle=\"Категория:Животные\sпо\sалфавиту\">Следующая\sстраница</a>")
    url_pattern: re.Pattern = re.compile("<a\shref=\"([^><]+)\"\stitle=\"Категория:Животные по алфавиту\">Следующая\sстраница</a>")
    group = re.search(url_pattern, answer)
    # for one_url in url:
    #     print(one_url)
    # print(group.group(1))
    url: str = "https://ru.wikipedia.org" + group.group(1)
    # print(url)
    # В извлечённой из html ссылке присутствует '&amp;'. HTTP запрос в этом случае будет возвращать не ту страницу.
    # Поэтому, произведена замена.
    url = re.sub('&amp;','&', url)
    await asyncio.sleep(sleep_time)
    return url


async def worker(url: str, params: dict, simbol: str, sleep_time: float = 0.001) -> int:
    """ Корутина, обрабатываемая параллельно. """
    answer: str = await request(url, params, sleep_time)
    animals: int = await get_animals_count(answer, simbol, sleep_time)
    next_url: str = await get_url_to_next_page(answer, sleep_time)
    # decoded = urllib.parse.unquote_plus(url)
    animals_count: int = 0
    if animals > 0:
        animals_count = await worker(next_url, {}, simbol, sleep_time)
    await asyncio.sleep(sleep_time)

    return animals + animals_count


def write_csv(filename: str, data: list[tuple[str]]) -> None:
    """ Запись csv файла. """
    pass


async def solution(sleep_time: float = 0.001) -> None:
    url: str = "https://ru.wikipedia.org/w/index.php"
    params = {'title': 'Категория:Животные_по_алфавиту', 'from': 'A'}

    # Создание списка с буквами русского и латинского алфавитов.
    alphabet: list[str] = [chr(value) for value in range(ord('А'), ord('Я') + 1)]
    alphabet.append('Ё')
    alphabet.extend([chr(value) for value in range(ord('A'), ord('Z') + 1)])
    # alphabet: list[str] = ["А"]

    tasks: list = [None for i in range(len(alphabet))]

    for i, simbol in enumerate(alphabet):
        # Перебор алфавита и запуск корутин
        print(simbol)


        params['from'] = simbol

        tasks[i] = asyncio.create_task(worker(url, copy.deepcopy(params), simbol, sleep_time), name=simbol)
        # tasks[i]

        # await asyncio.sleep(sleep_time)

    # params['from'] = 'Б'
    # Количество животных с разбивкой по буквам алфавита
    animals_count: dict[str, int] = {}
    # Список работающих задач
    runing_tasks: list = []

    while len(tasks) > 0:
        # Пока есть работающие задачи.

        # Подготавливаем список под ещё работающие задачи.
        # runing_tasks: set = set(tasks)

        for i, task in enumerate(tasks):
            # Переборка задач
            if task is not None:
                if not task.done():
                    # Если задача ещё не завершена
                    # Переносим её в список работающих задач.
                    runing_tasks.append(task)
                    pass
                else:
                    # Если задача завершена
                    try:
                        # Попытка получить результат работы задачи.
                        animals_count[task.get_name()] = task.result()
                        # tasks[i] = None
                    except asyncio.CancelledError:
                        # Задача была отменена
                        pass
                    except Exception:
                        # Задача завершилась ошибкой.
                        exception = task.exception()

            await asyncio.sleep(sleep_time)

        # "Обновляем" обрабатываемый список задач.
        tasks, runing_tasks = runing_tasks, []




    # if not task.done():
    #     await task

    # animals_count: int = 0
    # if task.done():
    #     try:
    #         animals_count = task.result()
    #     except asyncio.CancelledError:
    #         # Задача была отменена
    #         pass
    #     except Exception:
    #         # Задача завершилась ошибкой.
    #         exception = task.exception()

    for simbol in animals_count.keys():
        print(simbol, ':', animals_count[simbol])
    # print(animals_count)


if __name__ == '__main__':
    asyncio.run(solution(0.0001))