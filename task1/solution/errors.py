class StrictAnnotationTypeError(TypeError):
    """
    Ошибка в проверке типов.

    Это исключение возникает, когда аргумент, переданный в функцию,
    не соответствует аннотации.

    Attributes:
        func_name (str): Имя функции, в которой возникла ошибка.
        arg_name (str): Имя аргумента, вызвавшего ошибку.
        arg_type (type): Фактический тип аргумента.
        expected_type (type): Ожидаемый тип аргумента.

    """
    def __init__(self, func_name: str, arg_name: str, arg_type: type, expected_type: type):
        self.func_name = func_name
        self.arg_name = arg_name
        self.arg_type = arg_type
        self.expected_type = expected_type
        super().__init__(self.__str__())

    def __str__(self):
        return (f"Аргумент '{self.arg_name}' функции {self.func_name}() передан с аннотацией "
                f"{self.expected_type.__name__}, но на его фактический тип {self.arg_type.__name__}")


class StrictUnknownKeywordError(KeyError):
    """Ошибка неизвестного ключевого аргумента в проверке типов.

    Это исключение возникает, когда функция получает неожиданный ключевой аргумент.

    Attributes:
        arg_name (str): Имя неизвестного ключевого аргумента.
        func_name (str): Имя функции, в которой возникла ошибка.

    """
    def __init__(self, arg_name: str, func_name: str):
        self.arg_name = arg_name
        self.func_name = func_name
        super().__init__(self.__str__())

    def __str__(self):
        return f"{self.func_name}() не ожидает параметра с именем '{self.arg_name}'"
