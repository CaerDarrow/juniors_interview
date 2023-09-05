from abc import ABC, abstractmethod

from aiohttp import ClientSession


class Parser(ABC):
	@abstractmethod
	def _parse(self):
		raise NotImplementedError("Expected for '__parse' method")


class WikiPage:
	def __init__(self):
		self._url: str | None = None
		self._content: str | None = None
		self._session: ClientSession | None = None

	async def _read(self) -> None:
		if not self._url:
			raise ConnectionError(f"Url is not defined")
		async with ClientSession() as session:
			self._session = session
			r = await session.get(self._url)
			self._content = await r.text()
