import unittest
import constants
import WikiAnimalParser as parser


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        with parser.WikiAnimalParser() as test_parser:
            self.result_parse = test_parser.get_result()

    def test_with_correct_cnt_letter(self):
        self.assertEqual(self.result_parse['Й'], 4)

    def test_with_check_len_answer(self):
        self.assertEqual(len(self.result_parse), len(constants.russian_alphabet))
    
if __name__ == '__main__':
    unittest.main()
