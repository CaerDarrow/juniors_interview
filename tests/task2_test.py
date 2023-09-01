import re
from collections import defaultdict

import aiohttp
import pytest
import aioresponses
from bs4 import BeautifulSoup

from task2.solution import fetch_page


@pytest.mark.asyncio
async def test_fetch_page():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    # Имитируем страницу с одним животным на букву "А"
    mock_page_content = '''
    <div class="mw-category-group">
        <ul>
            <li><a>Антилопа</a></li>
        </ul>
    </div>
    '''

    # Имитация ответа сервера
    with aioresponses.aioresponses() as m:
        m.get(url, status=200, body=mock_page_content)

        async with aiohttp.ClientSession() as session:
            response_text = await fetch_page(session, url)
            soup = BeautifulSoup(response_text, 'html.parser')

            animals_count = defaultdict(int)
            for item in soup.select(".mw-category-group ul li a"):
                animal_name = item.get_text().strip()
                first_letter = animal_name[0].upper()
                if not re.match("[А-ЯЁ]", first_letter):
                    continue
                animals_count[first_letter] += 1

    # Проверка, что количество животных на букву "А" увеличилось на 1
    assert animals_count["А"] == 1
