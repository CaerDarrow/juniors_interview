# Тестовое задание

Общие требования:

- Для решения использовать python версии 3.9 или выше
- Для задания 2 можно использовать библиотеки, задачи 1 и 3 реализовать, используя встроенные средства языка
- Решение необходимо присылать в виде пулреквеста. Для реквеста надо форкнуть репозиторий по
  инструкции https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork.
  В реквесте укажите ваши данные.
- Решение каждой задачи должно быть в папке с ее условием, в файле `solution.py` или в модуле solution
- К каждой задаче необходимо написать тесты

# Удачи!

[Задача 1](task1/task1.md)   
[Задача 2](task2/task2.md)  
[Задача 3](task3/task3.md)

# How to run

### NOTE: for unix-system use `python3` and `pip3` if required or no venv

1. Install Python 3.10+
2. ```bash
    pip install -r requirements.txt
   ```
3. Move to right folder `cd task{1|2|3}/solution/`
4. Run tests with 
```bash 
pytest test{1|3}.py
``` 
for task 1 or 3 and `python test2.py` for task 2
5. For task 1 and 3 need to import `from solution import ...` decorator or function and use it. For task 2 just
   run `solution.py` (Needs Internet connection)

# Контакты

[Telegram](https://t.me/ugadai_s_3_raz)