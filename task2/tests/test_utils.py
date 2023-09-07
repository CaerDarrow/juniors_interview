import pytest
import requests
import requests_mock
from conftest import WIKI_URL

try:
    from service import utils
except ModuleNotFoundError:
    assert False, 'Убедитесь что в директории `service` есть файл `utils.py`'
except ImportError:
    assert False, 'Убедитесь что в директории `service` есть файл `utils.py`'


def test_find_tag_exception(soup):
    with pytest.raises(BaseException) as excinfo:
        utils.find_tag(soup, 'unexpected')
    assert excinfo.typename == 'ParserFindTagException', (
        'Функция `find_tag` в модуле `utils.py` в случае '
        'отсутствия искомого тэга'
        'должна выбросить нестандартное исключение `ParserFindTagException`'
    )
    msg = 'Не найден тег unexpected None'
    assert msg in str(excinfo.value), (
        f'Нестандартное исключение должно показывать сообщение: `{msg}`'
    )


def test_get_response(mock_session):
    with requests_mock.Mocker() as mock:
        mock.get(
            WIKI_URL + 'unexisting_page/',
            text='You are breathtaken',
            status_code=200
        )
        got = utils.get_response(
            mock_session,
            WIKI_URL + 'unexisting_page/'
        )
        assert isinstance(got, requests.models.Response), (
            'Убедитесь что функция `get_response` в модуле `utils.py` '
            'делает запрос к странице и возвращает ответ. \n'
            'Кстати: You are breathtaken!'
        )
