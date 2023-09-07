## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение  
Установить зависимости 
```
pip install -r requirements.txt
```
Парсер запускается командой
```
usage: python solution.py [-h] [-c] [-o {pretty,file}] {animal-info}

Для запуска с дефолтными значениями: python solution.py

positional arguments:
  {animal-info}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
### Режимы работы:
#### animal-info:
Формирует алфавитный список категорий животных (Буква алфавита, количество)
### Способы вывода данных:
#### pretty:
Выводит результат в виде таблицы
#### file:
Сохраняет данные в формате csv в директорию results

## Автор
Андрей Лабутин