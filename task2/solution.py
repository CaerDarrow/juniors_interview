import csv

from config import BEASTS_PAGE, BEASTS_XPATH, CYRILLIC_UPPER, FILENAME
from playwright.sync_api._generated import Page
from playwright.sync_api import sync_playwright


def go_to_next_page(page: Page) -> None:
    """Переход на следующую страницу на сайте"""

    page.locator(
        '//*[@id="mw-pages"]'
    ).get_by_text(
        'Следующая страница'
    ).first.click(timeout=3000)

    page.wait_for_load_state()


def parse(page: Page) -> dict[str, int]:
    """Парсинг списка животных с Википедии"""

    data = {x: 0 for x in CYRILLIC_UPPER}
    while True:
        beasts = page.locator(BEASTS_XPATH).all()
        try:
            for b in beasts:
                # Первая буква названия животного является ключом словаря
                data[b.inner_text()[0]] += 1
        except KeyError:
            # После кириллицы на сайте идёт латиница, поэтому разрываем цикл
            break
        try:
            go_to_next_page(page)
        except TimeoutError:
            break
    return data


def write_to_csv(data: dict[str, int]) -> None:
    """Экспорт в CSV"""

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data.items())


def main() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(BEASTS_PAGE)
        data = parse(page)
        write_to_csv(data)


if __name__ == '__main__':
    main()
