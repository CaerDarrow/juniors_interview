import mwclient
import csv


russian_chars = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
site, category = mwclient.Site("ru.wikipedia.org"), "Категория:Животные по алфавиту"
category_page = site.pages[category]
result = {char: 0 for char in russian_chars}
for animal in category_page:
    if animal.name[0] in russian_chars:
        result[animal.name[0]] += 1


with open("beasts.csv", "w", newline="", encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    for char, count in result.items():
        if count != 0:
            csv_writer.writerow([char, count])
