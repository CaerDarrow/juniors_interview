import unittest
from .solution import main, base_dir


class TestTask2(unittest.TestCase):
    load_path = base_dir / 'beasts.csv'

    def setUp(self) -> None:
        main(self.load_path)

    def test_csv_file(self):
        total_pages = 55

        with open(self.load_path) as file:
            beasts = file.readlines()
            self.assertEqual(len(beasts), total_pages)


if __name__ == '__main__':
    unittest.main()
