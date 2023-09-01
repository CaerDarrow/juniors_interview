import aiohttp
import pytest
import aioresponses
from task2.solution import fetch_page  # Импортируйте вашу функцию из вашего модуля


@pytest.mark.asyncio
async def test_fetch_page():
    url = 'https://example.com'

    with aioresponses.aioresponses() as m:
        m.get(url, payload={'data': 'some data'})

        async with aiohttp.ClientSession() as session:
            response = await fetch_page(session, url)

        assert response['data'] == 'some data'