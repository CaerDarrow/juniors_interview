import csv

import requests
from pydantic import BaseModel


class Member(BaseModel):
    ns: int
    title: str


API_URL = "https://ru.wikipedia.org/w/api.php"
params = {
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'cmtitle': 'Категория:Животные по алфавиту',
    'cmprop': 'title',
    'cmstartsortkeyprefix': '',
    'cmlimit': 500
}

animals = {}


def count_letter(letter: str):
    if animals.get(letter, None):
        animals[letter] = animals[letter] + 1
    else:
        animals[letter] = 1


def get_page_json() -> dict:
    with requests.get(url=API_URL, params=params) as res:
        if 200 > res.status_code >= 300:
            raise Exception("Wiki API error, try later")

        res_json = res.json()

        return res_json


def parse_write_json_members(members):
    for member in members:
        member = Member(**member)
        if member.ns == 0:
            title = member.title
            if title and type(title) == str:
                first_letter = title[0].capitalize()
                count_letter(first_letter)
            else:  # pass title if it's not str or empty
                print(f"Title {title} is broken, I'll pass it")
                continue


def fill_animals_count():
    con = True
    while con:
        res_json = get_page_json()

        if res_json.get('continue', None) is None:
            con = False
            next_page = None
        else:
            next_page = res_json['continue']['cmcontinue']

        query = res_json.get("query", None)
        if not query:  # check response
            raise Exception("Wiki error, please rewrite params and send request again")

        members = query.get("categorymembers", None)
        if not members:  # check response #2
            raise Exception("Wiki error, please rewrite params and send request again")

        parse_write_json_members(members)

        if con:
            params['cmcontinue'] = next_page


def write_to_csv():
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in sorted(animals.items()):  # IDK how to sort normal with `Ё`
            writer.writerow([k, v])


if __name__ == "__main__":
    fill_animals_count()
    write_to_csv()
