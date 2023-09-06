from solution import W
import unittest


a = {'W': 94, 'X': 177, 'Y': 46, 'Z': 213}

b = {'А': 1225, 'Б': 1686, 'В': 533}

c = {'А': 1225, 'Б': 1686, 'В': 533, 'Г': 1018, 'Д': 782, 'Е': 106, 'Ж': 413, 'З': 645, 'И': 354, 'Й': 4, 'К': 2321,
   'Л': 712, 'М': 1305, 'Н': 471, 'О': 810, 'П': 1801, 'Р': 588, 'С': 1826, 'Т': 1013, 'У': 272, 'Ф': 197, 'Х': 288,
   'Ц': 228, 'Ч': 692, 'Ш': 286, 'Щ': 159, 'Э': 223, 'Ю': 138, 'Я': 211, 'A': 3228, 'B': 1012, 'C': 2523, 'D': 1081,
   'E': 1039, 'F': 209, 'G': 692, 'H': 1091, 'I': 356, 'J': 86, 'K': 234, 'L': 1048, 'M': 1744, 'N': 838, 'O': 868,
   'P': 2702, 'Q': 45, 'R': 504, 'S': 1830, 'T': 1383, 'U': 142, 'V': 181, 'W': 94, 'X': 177, 'Y': 46, 'Z': 213}

d = {'А': 1225, 'Б': 1686, 'В': 533, 'Г': 1018, 'Д': 782, 'Е': 106, 'Ж': 413, 'З': 645, 'И': 354, 'Й': 4, 'К': 2321,
   'Л': 712, 'М': 1305, 'Н': 471, 'О': 810, 'П': 1801, 'Р': 588, 'С': 1826, 'Т': 1013, 'У': 272, 'Ф': 197, 'Х': 288,
   'Ц': 228, 'Ч': 692, 'Ш': 286, 'Щ': 159, 'Э': 223, 'Ю': 138, 'Я': 211}

e = {'В': 533, 'Г': 1018}

f = {'A': 3228, 'B': 1012, 'C': 2523, 'D': 1081, 'E': 1039, 'F': 209, 'G': 692, 'H': 1091, 'I': 356, 'J': 86, 'K': 234,
    'L': 1048, 'M': 1744, 'N': 838, 'O': 868, 'P': 2702, 'Q': 45, 'R': 504, 'S': 1830, 'T': 1383, 'U': 142, 'V': 181,
    'W': 94, 'X': 177, 'Y': 46, 'Z': 213}

g = {'W': 94, 'X': 177, 'Y': 46, 'Z': 213}

h = {'P': 2702, 'Q': 45, 'R': 504, 'S': 1830, 'T': 1383}

i = {'Ш': 286, 'Щ': 159, 'Э': 223, 'Ю': 138, 'Я': 211, 'A': 3228, 'B': 1012, 'C': 2523, 'D': 1081, 'E': 1039, 'F': 209}

j = {'O': 868, 'P': 2702}

k = {'Ё': 106, 'Ж': 413, 'З': 645}


class TestWikiAnimalsParsing(unittest.TestCase):

    def test_1(self):
        self.assertEqual(W.parser_launch(start_letter="W"), a)

    def test_2(self):
        self.assertEqual(W.parser_launch(stop_letter="В"), b)

    def test_3(self):
        self.assertEqual(W.parser_launch(), c)

    def test_4(self):
        self.assertEqual(W.parser_launch("А", "Я"), d)

    def test_5(self):
        self.assertEqual(W.parser_launch("Г", "В"), e)

    def test_6(self):
        self.assertEqual(W.parser_launch("A", "Z"), f)

    def test_7(self):
        self.assertEqual(W.parser_launch("W"), g)

    def test_8(self):
        self.assertEqual(W.parser_launch("T", "P"), h)

    def test_9(self):
        self.assertEqual(W.parser_launch("Ш", "F"), i)

    def test_10(self):
        self.assertEqual(W.parser_launch("O", "P"), j)

    def test_11(self):
        self.assertEqual(W.parser_launch("Ё", "З"), k)


if __name__ == '__main__':
    unittest.main()
