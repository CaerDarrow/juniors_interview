import os, shutil
import pytest
from solution import counter_parsed, save_csv, save_txt

# Было вручную подсчитано на трех страницах
link = {
    'url_test': 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Whalfera+wiszniewskii#mw-pages',
    'result': {'W': 39, 'Y': 46, 'X': 177, 'Z': 213},
}

data = {
    'path': 'tmp',
    'file_name': 'test.tmp',
    'dict': {'W': 39, 'Y': 46, 'X': 177, 'Z': 213},
    'result': 'W,39\nX,177\nY,46\nZ,213\n',
}

data_txt = {
    'path': 'tmp',
    'file_name': 'test.tmp',
    'dict': {'W': 39, 'Y': 46, 'X': 177, 'Z': 213},
    'result': 'W, 39\nX, 177\nY, 46\nZ, 213\n',
}

@pytest.mark.parametrize('url, result', [(link['url_test'], link['result'])])
def test_counter_parsed(url, result):
    """Проверка подсчета количества животных."""
    counter = counter_parsed(url)
    assert counter == result


@pytest.mark.parametrize('tmp_path, file_name, counter, result',
                         [(data['path'], data['file_name'],
                           data['dict'], data['result'])
                          ])
def test_save_csv(tmp_path, file_name, counter, result):
    """Проверка сохранение данных в csv-файл."""
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    full_name = os.path.join(tmp_path, file_name)
    save_csv(full_name, dict(sorted(counter.items())))

    with open(full_name, "r", encoding='utf-8') as file:
        actual_data = file.read()

    assert actual_data == result

    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)


@pytest.mark.parametrize('tmp_path, file_name, counter, result',
                         [(data_txt['path'], data_txt['file_name'],
                           data_txt['dict'], data_txt['result'])
                          ])
def test_save_txt(tmp_path, file_name, counter, result):
    """Проверка сохранение данных в txt-файл."""
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    full_name = os.path.join(tmp_path, file_name)
    save_txt(full_name, dict(sorted(counter.items())))

    with open(full_name, "r", encoding='utf-8') as file:
        actual_data = file.read()

    assert actual_data == result

    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
