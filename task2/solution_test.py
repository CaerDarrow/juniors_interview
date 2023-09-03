import solution 
import unittest
from unittest.mock import Mock


class SumTwoTestCase(unittest.TestCase):

    def test_calc_animals_on_page(self):
        first_a_tag = Mock()
        second_a_tag = Mock()
        third_a_tag = Mock()
        first_a_tag.text = "Абботины"
        second_a_tag.text = "Абелизавр"
        third_a_tag.text = "Абидозавр"
        first_li_tag = Mock()
        second_li_tag = Mock()
        third_li_tag = Mock() 
        first_li_tag.find = Mock(return_value=first_a_tag)
        second_li_tag.find = Mock(return_value=second_a_tag)
        third_li_tag.find = Mock(return_value=third_a_tag)
        tag_ul_mock = Mock()
        result_set = Mock()       
        result_set = iter([first_li_tag, second_li_tag, third_li_tag])
        tag_ul_mock.find_all = Mock(return_value = result_set)
        calc_animals_on_page = solution.calc_animals_on_page(tag_ul_mock, "А")
        self.assertEqual(calc_animals_on_page, True)



if __name__ == '__main__':
    unittest.main()
