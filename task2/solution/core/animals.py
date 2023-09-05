from colorama import Fore
import requests
from aiohttp import ClientSession

from ._core import WikiPage, Parser
from ._config import letter_url, main_url, list_from_url
from ._utils import parsing
from ._exceptions import ReadingDataError, ParsingError, EndOfDataError


class AnimalLetters(Parser):
	letters: list[str] = []

	def __init__(self):
		self._url = main_url
		self._content: str | None = None
		self.__read()
		self._parse()

	def __read(self) -> None:
		r = requests.get(self._url)
		if r.status_code != 200:
			raise ReadingDataError(f"Can't load animal letters list from '{self._url}'")
		self._content = r.text

	def _parse(self) -> None:
		letters = parsing.parse_animal_letters(self._content)
		if letters is None:
			raise ParsingError("Animal letters not defined")
		self.letters.extend(letters)

	def __repr__(self):
		return f"<AnimalLetters '{self.letters[0]} - {self.letters[-1]}'>"

	def __str__(self):
		return str(self.__repr__())

	def __iter__(self):
		return iter(self.letters)


class Animal(WikiPage, Parser):
	_session: ClientSession  # may be used
	_content: str

	def __init__(self, letter: str):
		"""
		_url - первая страница
		"""
		super().__init__()
		if len(letter) > 1:
			raise ValueError("Incorrect letter length")
		self.letter = letter.upper()
		self._url = letter_url.format(self.letter)
		self.animals: list[str] = []

	def __str__(self):
		return f"<Animals by '{self.letter}'>"

	def __len__(self):
		return len(self.animals)

	def __getitem__(self, item):
		return self.animals[item]

	async def _parse(self) -> None:
		counter = 0
		while True:
			await self._read()
			content_without_html = parsing.clear_html_tags(self._content)
			try:
				if counter == 0:
					searching_args = (content_without_html, self.letter)
				else:
					searching_args = (content_without_html, self.letter, True)  # exclude first
				animals = parsing.search_animals_on_page(*searching_args)
			except EndOfDataError:
				break
			self.animals.extend(animals)
			self._get_next_page_url()
			counter += 1
		self.animals = list(set(self.animals))  # есть повторения - долго не буду разбираться, почему возникают

	def _get_next_page_url(self) -> None:
		try:
			last_animal = self.animals[-1]
		except IndexError:
			raise ParsingError("Can't define next page url")
		formatted_animal_string = "+".join(last_animal.split())
		self._url = list_from_url.format(
			letter_1=self.letter, letter_2=self.letter, animal=formatted_animal_string
		)

	async def get(self) -> None:
		print(Fore.RESET + Fore.YELLOW + "SCANNING:\t" + Fore.RESET + self.letter + "\t...")
		await self._parse()
