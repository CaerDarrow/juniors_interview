import unittest
from solution import fetch_animals, save_to_csv
import os


class TestFetchAnimals(unittest.TestCase):
    def test_fetch_animals(self):
        # Test that animals are fetched correctly
        animals = fetch_animals()
        self.assertTrue(isinstance(animals, list))
        self.assertTrue(len(animals) > 0)
        for animal_dict in animals:
            self.assertTrue(isinstance(animal_dict, dict))


class TestSaveToCSV(unittest.TestCase):
    def test_save_to_csv(self):
        # Test that animals are saved to CSV file correctly
        animals = [
            {"A": 10},
            {"B": 20},
            {"C": 30},
        ]
        save_to_csv(animals)

        # Check if the CSV file was created
        self.assertTrue(os.path.exists("animals.csv"))


if __name__ == "__main__":
    unittest.main()
