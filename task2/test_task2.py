import unittest
from .solution import main


class TestTask2(unittest.TestCase):

    def setUp(self) -> None:
        main()

    def test_csv_file(self):
        with open('beasts.csv', encoding='utf-8-sig') as file:
            beasts = file.readlines()
            self.assertEqual(len(beasts), 55)



if __name__ == '__main__':
    unittest.main()