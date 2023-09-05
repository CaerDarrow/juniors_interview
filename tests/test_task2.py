import asyncio
import aiohttp
import pytest
from task2.solution import get_page_data, gather_data, animals_count


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_get_page_data():
    async with aiohttp.ClientSession() as session:
        letter = 'А'
        await get_page_data(session, letter)
        assert animals_count[letter] != 0


@pytest.mark.asyncio
async def test_gather_data(event_loop):
    await gather_data()


@pytest.mark.asyncio
async def test_get_page_data_invalid_input():
    with pytest.raises(KeyError):
        async with aiohttp.ClientSession() as session:
            letter = 'Z'
            await get_page_data(session, letter)
