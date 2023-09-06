import wikipediaapi
import csv


def get_categorymembers(categorymembers):
    alphabet = {}

    for c in categorymembers.values():
        if not c.ns == wikipediaapi.Namespace.CATEGORY:
            alphabet[c.title[0]] = alphabet.get(c.title[0], 0) + 1

    return alphabet


def write_csv(data):
    with open('beasts.csv', 'w', encoding="utf-8") as csvfile:
        for key in data.keys():
            csvfile.write("%s,%s\n" % (key, data[key]))


def main():
    wiki_wiki = wikipediaapi.Wikipedia('juniors-tets (rh26157@gmail.com)', 'ru')
    cat = wiki_wiki.page("Категория:Животные по алфавиту")

    data = get_categorymembers(cat.categorymembers)
    write_csv(data)


if __name__ == '__main__':
    main()

