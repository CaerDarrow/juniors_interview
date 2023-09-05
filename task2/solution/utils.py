import asyncio
import csv

from colorama import Fore, Back, Style

from core.animals import AnimalLetters, Animal
import config


async def aggregate_animal_groups(letters: AnimalLetters) -> list[Animal]:
	animals = [Animal(letter) for letter in letters]
	await asyncio.gather(*[animal.get() for animal in animals])
	return animals


def write_result(animals: list[Animal]) -> None:
	result_dict = {
		animal.letter: len(animal) for animal in animals
	}
	with open(config.OUTPUT_FILE, "w", encoding="utf-8") as file_out:
		writer = csv.writer(file_out)
		writer.writerows(result_dict.items())
	print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "IT'S DONE =)" +
		  Back.RESET + Fore.RESET + f" \tCheck the result at ../{config.OUTPUT_FILE}")
