import unittest
import os
import csv


class TestParser(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.isfile("beasts.csv"))

    def test_no_zeros(self):
        with open("beasts.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                _, count = row
                count = int(count)
                self.assertNotEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
