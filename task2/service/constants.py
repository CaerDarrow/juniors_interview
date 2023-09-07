from pathlib import Path

BASE_DIR = Path(__file__).parent

WIKI_URL = 'https://ru.wikipedia.org'

ANIMAL_URL = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'

ANIMAL_PARSE_MODE = 'animal-info'

FIRST_CHAR = ord('А')

CATEGORY_CHARS = ''.join([chr(i) for i in range(FIRST_CHAR, FIRST_CHAR + 32)])

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

DT_FORMAT = '%d.%m.%Y %H:%M:%S'

CSV_FILE_NAME = 'beasts.csv'

LOG_PATH = BASE_DIR / 'logs'

LOG_FILE = LOG_PATH / 'parser.log'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

TABLE_HEADER_STATUS_COUNT = ('Буква', 'Количество')

TABLE_FOOTER_STATUS_TOTAL = 'Total'
