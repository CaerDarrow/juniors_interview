from pathlib import Path

try:
    from service import constants
except ModuleNotFoundError:
    assert False, 'Убедитесь что в директории `service` есть файл `constants.py`'
except ImportError:
    assert False, 'Убедитесь что в директории `service` есть файл `constants.py`'


def test_costants_file():
    assert hasattr(constants, 'WIKI_URL'), (
        'В модуле `constants.py` нет переменной `WIKI_URL`'
    )
    assert isinstance(constants.WIKI_URL, str), (
        'В модуле `constants.py` тип переменной `WIKI_URL` '
        'должен быть `str`'
    )
    assert hasattr(constants, 'BASE_DIR'), (
        'В модуле `constants.py` нет переменной `BASE_DIR`'
    )
    assert isinstance(constants.BASE_DIR, Path), (
        'В модуле `constants.py` тип переменной `BASE_DIR` должен быть `Path`'
    )
