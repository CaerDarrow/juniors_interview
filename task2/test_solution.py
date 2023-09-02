import csv
import unittest
from solution import get_animal_list, count_animals


class AnimalListTest(unittest.TestCase):
    def test_get_animal_list(self):
        animals = get_animal_list()
        self.assertIsInstance(animals, list, "Функция должна возвращать список")
        self.assertGreater(len(animals), 0, "Список животных должен быть не пустым")

    def test_count_animals(self):
        # Создаем временный список животных для тестирования
        animals = ['Акула', 'Бабка альпийская', 'Ворон', 'Гладкохвостый скат', 'Диплодок']

        # Вызываем функцию count_animals() для тестирования
        count_animals(animals)

        # Проверяем, что CSV файл был создан и содержит корректные данные
        with open('fauna.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            self.assertEqual(len(rows), 5, "Необходимо указать правильное количество строк в CSV файле")

            expected_data = [
                ['А', '1'],
                ['Б', '1'],
                ['В', '1'],
                ['Г', '1'],
                ['Д', '1']
            ]

            self.assertEqual(rows, expected_data, "Данные в CSV файле должны соответствовать ожидаемым значениям")


if __name__ == '__main__':
    unittest.main()

print("Все тесты завершены успешно")