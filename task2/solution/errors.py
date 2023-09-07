class WrongSymbolInLetters(Exception):
    def __init__(self, letter):
        self.letter = letter

    def __str__(self):
        return f"Символ {self.letter} не может быть обработан, так как он не входит ни в кириллицу, ни в латиницу"
