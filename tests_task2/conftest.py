import sys
from pathlib import Path
from typing import Optional
from unittest.mock import Mock

import pytest
from requests_cache.models.response import OriginalResponse
from requests_cache.session import CachedSession

from .data import TEXT1, TEXT2
from task2 import mock_settings

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))
START_URL = 'https://harry_potter_creatures.ru'
LAST_URL = 'https://harry_potter_creatures.ru/page2'
mock_settings.is_mock = True


@pytest.fixture(scope="class")
def mock_session():
    return Mock()


def get_response_mock(
        _: CachedSession, url: str) -> Optional[OriginalResponse]:
    response = Mock()
    if url == START_URL:
        response.text = TEXT1
    elif url == LAST_URL:
        response.text = TEXT2
    else:
        response.text = ''
    return response
