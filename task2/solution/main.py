import asyncio

from core.animals import AnimalLetters
from utils import aggregate_animal_groups, write_result


async def main():
	"""
	Логика работы такова:
	- Определение букв, на которые начинаются названия животных (а вдруг добавят букву "Ё" или "Й"?);
	- Парсинг животных по каждой букве: животные сохраняются в коллекцию (при желании можно будет ими воспользоваться
	 иным образом, помимо подсчета);
	- Запись результатов в итоговый файл.

	ПРИМ.: написать тесты к этой задаче - дело небыстрое. Поэтому я бы с радостью их написал, но есть
	 работа с коммерческими проектами, которые не ждут =(
	"""
	letters = AnimalLetters()
	animals = await aggregate_animal_groups(letters)
	write_result(animals)


if __name__ == "__main__":
	asyncio.run(main())
