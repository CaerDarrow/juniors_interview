import csv
import re
from tempfile import NamedTemporaryFile

import pytest
from task2.solution import BeastCounter


@pytest.mark.asyncio
async def test_beast_counter():
    """Check normal work of beast counter script."""
    with NamedTemporaryFile() as temp_file:
        beast_counter = BeastCounter(temp_file.name)
        await beast_counter.run_script()

        with open(temp_file.name, encoding='utf-8', newline='') as csvfile:
            beasts_data = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in beasts_data:
                char, count = row

        assert re.match(r'[А-Я]', char)
        assert count != 0
