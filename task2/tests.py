import unittest
from unittest.mock import Mock, patch, mock_open, call
from solution import get_beasts_name, write_to_file


class TestTask2(unittest.TestCase):
    @patch('solution.requests.get')
    def test_get_beasts_name(self, mock_get):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            'query': {
                'categorymembers': [
                    {'title': 'Лев'},
                    {'title': 'Тигр'},
                    {'title': 'Слон'},
                    {'title': 'Леопард'},
                ]
            }
        }
        mock_get.return_value = response_mock

        beasts, count = get_beasts_name()
        self.assertEqual(beasts, {'Л': 2, 'Т': 1, 'С': 1})
        self.assertEqual(count, 4)

    @patch('solution.open', new_callable=mock_open)
    def test_write_to_file(self, mock_file_open):
        beasts_data = {"Лев": 2, "Тигр": 3}

        write_to_file(beasts_data)

        mock_file_open.assert_called_once_with('beasts.csv', 'w', newline='', encoding='utf-8')
        handle = mock_file_open()
        calls = [call('Лев,2\r\n'), call('Тигр,3\r\n')]
        handle.write.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
