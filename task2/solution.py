# работу не ищу, было просто скучно :)
# Это синхронное чудовище вытаскивает все данные без сторонних модулей, используя лишь встроенные средства самого питона
# требует python3 >= 3.10 из-за тайпинга

import csv
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from email.message import Message
from typing import Any


BASE_URL = "https://ru.wikipedia.org"
ANIMAL_PATH = "/wiki/Категория:Животные_по_алфавиту"


@dataclass
class Response:
    body: str
    headers: Message
    status: int
    error_count: int = 0

    def json(self) -> dict[str, Any]:
        try:
            output = json.loads(self.body)
        except json.JSONDecodeError:
            output = {}
        return output


def request(
    url: str,
    data: dict = None,
    params: dict = None,
    headers: dict = None,
    method: str = "GET",
    data_as_json: bool = True,
    error_count: int = 0,
) -> Response:
    if not url.casefold().startswith("http"):
        raise urllib.error.URLError("Incorrect and possibly insecure protocol in url")
    method = method.upper()
    request_data = None
    headers = headers or {}
    data = data or {}
    params = params or {}
    headers = {"Accept": "application/json", **headers}

    if method == "GET":
        params = {**params, **data}
        data = None

    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True, safe="/")

    if data:
        if data_as_json:
            request_data = json.dumps(data).encode()
            headers["Content-Type"] = "application/json; charset=UTF-8"
        else:
            request_data = urllib.parse.urlencode(data).encode()

    http_request = urllib.request.Request(
        url, data=request_data, headers=headers, method=method
    )

    try:
        with urllib.request.urlopen(http_request) as http_response:
            response = Response(
                headers=http_response.headers,
                status=http_response.status,
                body=http_response.read().decode(
                    http_response.headers.get_content_charset("utf-8")
                ),
            )
    except urllib.error.HTTPError as error:
        response = Response(
            body=str(error.reason),
            headers=error.headers,
            status=error.code,
            error_count=error_count + 1,
        )

    return response


class WikiParser:

    def __init__(self):
        self.data = []
        self.animals_count = self._count_animals_by_letter()

    def get_next_page(self, raw_string: str) -> str | None:
        next_page_template = re.compile('Предыдущая страница.*<a href=.*>Следующая страница<')
        try:
            next_page = next_page_template.findall(raw_string)[0]
            return (
                next_page
                .replace('Предыдущая страница', "")
                .replace("</a>", "")
                .replace('<a href="', "")
                .replace('"title="Категория:Животные по алфавиту">Следующая страница<', "")
                .replace("amp;", "")
                .replace("(", "")
                .replace(")", "")
                .strip(" ")
            )
        except IndexError:
            return None

    def get_data(self, url: str) -> Response:
        animals_template = re.compile('title=\"[А-я -]+\">[A-я -]+</a></li>')
        animal_name_template = re.compile('>[А-я -]*<')
        animals_data = request(url)
        animals = animals_template.findall(animals_data.body)
        for row_string in animals:
            try:
                animal = animal_name_template.findall(row_string)[0].strip("<").strip(">")
                self.data.append(animal)
            except IndexError:
                pass
        return animals_data

    def _count_animals_by_letter(self) -> dict[str, Any]:
        animals_url = BASE_URL + urllib.parse.quote(ANIMAL_PATH)
        self.get_data(animals_url)

        response = request(animals_url)
        next_page = BASE_URL + self.get_next_page(response.body)

        while next_page:
            page = self.get_data(next_page)
            if next_page := self.get_next_page(page.body):
                next_page = BASE_URL + next_page

        return dict(sorted(Counter([animal[0] for animal in set(self.data)]).items()))


if __name__ == '__main__':

    wiki_parser = WikiParser()
    animals_count = wiki_parser.animals_count

    with open("beasts.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for letter, count in animals_count.items():
            writer.writerow([letter, count])
