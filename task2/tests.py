import os
from collections import namedtuple
from task2.solution import get_animals_from_page, get_animals_count


test_dir_path = os.path.dirname(__file__)
test_page_path = os.path.join(test_dir_path, 'test_data/page.html')
test_last_page_path = os.path.join(test_dir_path, 'test_data/page_last.html')


Response = namedtuple('Response', ['content'])


def test_get_animals_for_letter(mocker):
    with open(test_page_path, 'rb') as f:
        content = f.read()
    mock_response = Response(content=content)
    m = mocker.patch('requests.get')
    m.return_value=mock_response
    animal_names, next_page_url = get_animals_from_page('http://test')
    m.assert_called_once_with(url='http://test')
    assert len(animal_names) == 200
    assert next_page_url == '/next_page.php'
    assert animal_names[0] == 'Аардоникс'
    assert animal_names[-1] == 'Азиатские щучки'


def test_get_animals_for_letter_last_page(mocker):
    with open(test_last_page_path, 'rb') as f:
        content = f.read()
    mock_response = Response(content=content)
    m = mocker.patch('requests.get')
    m.return_value=mock_response
    animal_names, next_page_url = get_animals_from_page('http://test')
    m.assert_called_once_with(url='http://test')
    assert len(animal_names) == 200
    assert next_page_url is None
    assert animal_names[0] == 'Аардоникс'
    assert animal_names[-1] == 'Азиатские щучки'


def test_get_animals_count(mocker):
    m = mocker.patch('task2.solution.get_animals_from_page')
    m.side_effect = [
        (['лягушка', 'тигр'], '/next1.php'),
        (['кошка', 'собака'], '/next2.php'),
        (['лось', 'кот'], None),
    ]
    animals_count = get_animals_count('http://test/animals.php', 'http://test')
    assert animals_count == {'Л': 2, 'Т': 1, 'К': 2, 'С': 1}
    assert m.call_count == 3
    expected_calls = [mocker.call('http://test/animals.php'), mocker.call('http://test/next1.php'),
                      mocker.call('http://test/next2.php')]
    m.assert_has_calls(expected_calls)

