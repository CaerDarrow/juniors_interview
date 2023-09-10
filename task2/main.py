from solution import save_animal_list


if __name__ == '__main__':
    page_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    save_animal_list(page_url, 'https://ru.wikipedia.org', 'beasts.csv')
