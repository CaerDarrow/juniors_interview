import csv
import logging

from prettytable import PrettyTable

from .constants import BASE_DIR, CSV_FILE_NAME


def console_output(results, *args):
    """Дефолтный вывод в консоль."""
    print(
        '\n'.join(
            f'{key}={value}' for key, value in results.items()
        )
    )


def pretty_output(results, *args):
    """Вывод результата в виде таблицы."""
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    """Запись результатов в файл."""
    results_dir = BASE_DIR.parent
    file_path = results_dir / CSV_FILE_NAME
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_NONE)
        writer.writerows(results.items())
    logging.info(f'Файл с результатами был сохранён: {file_path}')


OUTPUT_TO_FUNCTION = {
    'pretty': pretty_output,
    'file': file_output,
    'console': console_output,
}


def control_output(results, cli_args):
    OUTPUT_TO_FUNCTION.get(cli_args.output, file_output)(results, cli_args)
