import re

from .._exceptions import EndOfDataError


def clear_html_tags(html: str) -> str:
	html_without_tags = re.sub(r'(\<(/?[^>]+)>)', '', html)
	return html_without_tags


def parse_animal_letters(html: str) -> list[str] | None:
	html_without_tags = clear_html_tags(html)
	res = re.search(r'(в начало[А-Я]{,35})', html_without_tags).group(1)
	res = res.replace("в начало", "")
	res = sorted(list(set(res)))
	return res


def search_animals_on_page(text: str, startswith: str, exclude_first: bool = False) -> list[str]:
	"""
	:param exclude_first: исключить первое название животного (чтобы избежать повторений в итоговом списке)
	 - при переходе по url по названию животного оно выводится первым; а в качестве названия беру последнее из
	  уже сохраненных
	"""
	if len(startswith) > 1:
		raise ValueError("Expected for 1 start letter")
	try:
		regex = r'\n' + startswith + r'\D+\n -->'
		res = re.findall(regex, text)[0]
	except IndexError:
		raise EndOfDataError("Parsing animal strings error - needs at least 1 string")
	splitted_res = res.split("\n")
	if exclude_first:
		splitted_res = splitted_res[1:]
	cleaned_res = []
	for s in splitted_res:
		if any(s):
			if s.startswith(startswith):  # хз, почему, но RE включает и названия с другими буквами тоже
				if "(П" in s:
					s = s.split("(", 1)[0]
					cleaned_res.append(s)
					break
				cleaned_res.append(s)
	return cleaned_res
