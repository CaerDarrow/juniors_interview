import os
from unittest import mock

import pytest
from bs4 import BeautifulSoup as bs
from solution import (
    Constants,
    _create_result_dict,
    _union_sets_with_animals,
    create_csv_file,
    get_letter_links,
    get_soup_from_request,
    get_table_lines_from_soup,
    handle_data,
)


@pytest.fixture()
def animal_data():
    return [set(['Лев', 'Лось']), set(['Собака', 'Слон'])]


def test_constants():
    assert Constants.URL == "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    assert Constants.RESULT_FILE_NAME == 'beasts.csv'
    assert Constants.ENG_LETTER_A == 'A'
    assert Constants.FROM_SECOND_LINE == 1
    assert Constants.FIRST_LETTER_ID == 0


def test_get_soup_from_request():
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"<html><body></body></html>"

        soup = get_soup_from_request(request_url="https://example.com")

        assert soup is not None


def test_get_table_lines_from_soup():
    soup_data = bs(
        """
        <table class='plainlinks'>
            <tr>
                <td>Row 1</td>
            </tr>
            <tr>
                <td>Row 2</td>
            </tr>
        </table>
        """,
        "html.parser"
    )
    lines = get_table_lines_from_soup(soup_data=soup_data)

    assert len(lines) == 2


def test_get_letter_links():
    mock_line_1 = bs(
        """
        <tr>
            <td>
                <a href='/link1'>Link 1</a>
            </td>
        </tr>
        """,
        "html.parser"
    )
    mock_line_2 = bs(
        """
        <tr>
            <td>
                <a href='/link2'>Link 2</a>
            </td>
        </tr>
        """,
        "html.parser"
    )
    table_lines = [mock_line_1, mock_line_2]

    links = get_letter_links(table_lines=table_lines)

    assert len(links) == 1  # coz table_lines[Constants.FROM_SECOND_LINE:]
    assert '/link2' in links


def test_handle_data(animal_data):
    result = handle_data(data=animal_data)

    assert result['Л'] == 2
    assert result['С'] == 2


def test_create_result_dict():
    result_dict = _create_result_dict()

    assert len(result_dict) == 32
    assert 'А' in result_dict
    assert 'Я' in result_dict


def test_union_sets_with_animals(animal_data):
    result_set = _union_sets_with_animals(data=animal_data)

    assert len(result_set) == 4
    assert 'Лев' in result_set
    assert 'Собака' in result_set


def test_create_csv_file(tmp_path):
    file_path = tmp_path / "test.csv"
    results = {'А': 3, 'Б': 5}

    create_csv_file(file_name=str(file_path), results=results)

    assert file_path.exists()

    with open(file_path, "r", encoding="utf-8") as csv_file:
        content = csv_file.read()
        assert "А,3" in content
        assert "Б,5" in content

    os.remove(file_path)
