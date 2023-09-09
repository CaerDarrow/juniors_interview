import unittest
import solution


class AnimalParserTest(unittest.TestCase):
     
    def test_statuscode_nonepage(self):
        self.assertEqual(solution.responce.status_code, 200)
        self.assertNotEqual(solution.get_animal_list(solution.soup), "")

    def test_firstletter_equal(self):
        first_letter = solution.get_animal_list(solution.soup)
        self.assertEqual(first_letter[0].text[0], 'А')

    def test_nonlist(self):
        self.assertNotEqual(solution.get_animal_list(solution.soup), [])

    def test_write_csv(self):
        data = {"A": 10, "B": 20, "C": 30}
        expected_csv = "A,10\nB,20\nC,30\n"
        solution.write_to_csv(data)

        with open("beasts.csv", "r") as file:
            actual_csv = file.read()
        self.assertEqual(actual_csv, expected_csv)


if __name__ == '__main__':
    unittest.main()

