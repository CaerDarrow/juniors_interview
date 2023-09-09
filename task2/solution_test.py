import csv


class TestAnimals:
    def test_one(self):
        with open('animal.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            assert next(reader) == ['А', '1118']
            assert next(reader) == ['Б', '950']

    def test_two(self):
        with open('animal.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            next(reader)
            assert next(reader) == ['Б', '950']
