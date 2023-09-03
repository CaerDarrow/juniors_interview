import bs4
import requests
import csv


def get_letters_and_counts() -> dict[str, int]:
    start_page_url = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'
    html = requests.get(start_page_url).text

    letters_and_counts = {}

    while True:
        doc = bs4.BeautifulSoup(html)
        content = doc.find('div', {'id': 'mw-pages'})
        groups = content.find_all('div', {'class': 'mw-category-group'})
        
        stop = False
    
        for group in groups:
            letter = group.find('h3').text

            if ('А' <= letter <= 'Я') is False:
                stop = True
                break
            
            li_elements = group.find('ul').find_all('li')
            child_count = len(li_elements)

            if letter not in letters_and_counts:
                letters_and_counts[letter] = 0
                
                print(f'Start parse {letter}. All found {sum(letters_and_counts.values())} elements')

            letters_and_counts[letter] += child_count
            
        if stop:
            break

        next_page_url = 'https://ru.wikipedia.org' + content.find('a', string='Следующая страница')['href']
        html = requests.get(next_page_url).text
        
    return letters_and_counts


def fill_file(file_path: str, rows: list[list]):
    with open(file_path, 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        
        for row in rows:
            writer.writerow(row)


letters_and_counts = get_letters_and_counts()
fill_file('./task2/res.csv', letters_and_counts.items())
