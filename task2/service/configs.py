import argparse
import logging
from logging.handlers import RotatingFileHandler

from .constants import (ANIMAL_PARSE_MODE, DT_FORMAT, LOG_FILE, LOG_FORMAT,
                       LOG_PATH)


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(
        description='Парсер Wiki документации по категориям животных'
    )
    parser.add_argument(
        'mode',
        choices=available_modes,
        default=ANIMAL_PARSE_MODE,
        const=ANIMAL_PARSE_MODE,
        nargs='?',
        help='Режимы работы парсера'
    )
    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=('pretty', 'file'),
        help='Дополнительные способы вывода данных'
    )
    return parser


def configure_logging():
    LOG_PATH.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10 ** 6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
