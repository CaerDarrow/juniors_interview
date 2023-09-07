import logging
from collections import defaultdict
from requests import RequestException
from urllib.parse import urljoin

import requests_cache
from tqdm import tqdm

from .configs import configure_argument_parser, configure_logging
from .constants import ANIMAL_PARSE_MODE, ANIMAL_URL, CATEGORY_CHARS, WIKI_URL
from .exceptions import DOMQueryingException, ParserCharsException, ParserFindTagException
from .outputs import control_output
from .utils import find_tag, find_tag_all, get_soup_by_url, select_one_tag


def animal_info(session):
    "Возвращает справочник по категориям животных."
    categories = defaultdict(int)
    url = ANIMAL_URL
    try:
        progress_bar = tqdm(total=len(CATEGORY_CHARS))
        parsed_chars = set()
        while True:
            soup = get_soup_by_url(session, url)
            category_info = find_tag(
                soup,
                "div",
                {"class": "mw-category mw-category-columns"}
            )
            category_group = find_tag_all(
                category_info,
                "div",
                {"class": "mw-category-group"}
            )
            for div in category_group:
                group_char = div.find("h3").text.upper()
                if group_char not in CATEGORY_CHARS:
                    raise ParserCharsException
                links = div.find_all("a")
                categories[group_char] += len(links)
                parsed_chars.add(group_char)
                progress_bar.update(len(parsed_chars))
            next_page_url = select_one_tag(
                    soup,
                    '#mw-pages a:-soup-contains("Следующая страница")'
            )['href']
            url = urljoin(WIKI_URL, next_page_url)
    except (ParserFindTagException, RequestException):
        logging.exception(
            'Ошибка получения информации для парсинга!'
        )
    except DOMQueryingException:
        logging.warning(
            'Ссылка на следующую страницу не найдена! [URL={next_page_url}]'
        )
    except ParserCharsException:
        logging.info(
            'Выборка по категориям из алфавита завершена!'
        )
    finally:
        progress_bar.close
    return categories


MODE_TO_FUNCTION = {
    ANIMAL_PARSE_MODE: animal_info,
}


def parse_wiki_animals():
    "Парсинг категорий животных."
    configure_logging()
    logging.info('Парсер запущен!')
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')
    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()
    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    parse_wiki_animals()
