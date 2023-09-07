import csv
from pathlib import Path

from .conftest import START_URL
from task2.solution import amount_animals, calculate_beasts

BASE_DIR = Path(__name__).absolute().parent
MAIN_DIR = BASE_DIR / 'task2'


def test_csv_files():
    csv_files = [
        file for file in MAIN_DIR.iterdir() if file.match('*.csv')
    ]

    assert len(csv_files), (
        'В папке task2 не обнаружен csv файл. '
        'Сохраните результаты работы парсера '
        'в csv-файле в папке task2.'
    )
    assert len(csv_files) == 1, (
        'В папке task2 обнаружено несколько csv файлов.'
    )
    assert 'beasts.py' not in csv_files, (
        'В папке task2 не обнаружен файл beasts.py. '
        'Сохраните результаты работы парсера '
        'в csv-файле в папке task2.'
    )
    beasts = csv_files[0]
    with open(beasts, 'r', encoding="utf-8") as f:
        file_reader = csv.reader(f, delimiter=",")
        for line in file_reader:
            assert len(line) == 2, (
                'Все строки в файле beasts.py должны иметь 2 аргумента.'
            )
            assert line[0].isalpha(), (
                'Все ключи в файле beasts.py должны быть заглавными буквами.'
            )
            assert line[0].isupper(), (
                'Все ключи в файле beasts.py должны быть заглавными буквами.'
            )
            assert line[1].isnumeric(), (
                'Все значения в файле beasts.py должны быть целыми числами.'
            )


def test_calculate_beasts(mock_session):
    calculate_beasts(mock_session, START_URL)
    assert amount_animals == {'Г': 2, 'Е': 1, 'Н': 1, 'П': 1}, (
        f"Результат выполнения функции calculate_beasts {amount_animals} "
        "не соответсвует ожидаемому {'Г': 2, 'Е': 1, 'Н': 1, 'П': 1}"
    )
