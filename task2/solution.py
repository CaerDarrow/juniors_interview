import urllib.request
import json
import csv
import unittest

def main_f():
    titles = []
    cont = 0
    while cont is not None:
        pages = urllib.request.urlopen("https://ru.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&format=json&cmlimit=max&cmtype=page&cmcontinue=" + str(cont))
        data = json.load(pages)
        query = data['query']
        category = query['categorymembers']
        for x in category:
            titles.append(x['title'])
        if 'continue' in data:
            cont = data['continue']['cmcontinue']
        else:
            cont = None
    whatsup = {}
    for title in titles:
        letter = title[0]
        if letter in whatsup:
            whatsup[letter]+=1
        else:
            whatsup[letter] = 1
    with open('beasts.csv', 'w') as f:
        writer = csv.writer(f)
        for letter, number in whatsup.items():
            writer.writerow([letter, number])


class TestCsvResult(unittest.TestCase):
    def test_csv_file(self):
        data = {'А': 1226, 'Б': 1687, 'В': 533, 'К': 2320, 'Г': 1016, 'П': 1801, 'Д': 784, 'Е': 103, 'Ё': 2, 'О': 811, 'Ж': 412, 'Я': 213, 'З': 645, 'И': 354, 'Й': 4, 'С': 1826, 'Л': 712, 'М': 1307, 'Н': 471, 'Р': 588, 'Т': 1012, 'У': 272, 'Ф': 197, 'Х': 288, 'Ц': 228, 'Ч': 692, 'Ш': 286, 'Щ': 159, 'Э': 223, 'Ю': 138, 'A': 3228, 'B': 1010, 'C': 2522, 'D': 1081, 'E': 1038, 'F': 209, 'G': 691, 'H': 1091, 'I': 356, 'J': 86, 'K': 234, 'L': 1047, 'M': 1744, 'N': 838, 'O': 868, 'P': 2699, 'Q': 45, 'R': 504, 'S': 1828, 'T': 1382, 'U': 142, 'V': 181, 'W': 94, 'X': 177, 'Y': 46, 'Z': 213}
        with open('beasts.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.assertEqual(int(row[1]), data[row[0]])

if __name__ == '__main__':
    main_f()
    unittest.main()