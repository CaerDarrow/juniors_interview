class DOMQueryingException(Exception):
    """Вызывается, когда парсер не может найти теги используя CSS селектор."""
    pass


class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ParserCharsException(Exception):
    """Вызывается, когда парсер обрабатывает категории не из алфавита."""
    pass
