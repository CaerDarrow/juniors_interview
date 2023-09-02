import csv
import unittest

from solution import parse_write_json_members, write_to_csv


class TestAnimal(unittest.TestCase):
    def test_add_members(self):
        members = [{'ns': 0, 'title': 'Аардоникс'},
                   {'ns': 0, 'title': 'Абботины'},
                   {'ns': 0, 'title': 'Абелизавр'},
                   {'ns': 0, 'title': 'Абелизавриды'},
                   {'ns': 0, 'title': 'Абидозавр'},
                   {'ns': 0, 'title': 'Абингдонская слоновая черепаха'},
                   {'ns': 0, 'title': 'Бабайка'},
                   {'ns': 0, 'title': 'Домовой'}]
        parse_write_json_members(members)
        write_to_csv()
        with open('beasts.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        expected_data = [
            ['А', '6'],
            ['Б', '1'],
            ['Д', '1']
        ]
        self.assertEqual(rows, expected_data, "rows must be equal")


if __name__ == "__main__":
    unittest.main()
