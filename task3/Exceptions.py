class ListOddLength(Exception):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return '{} the list is invalid because it has an odd length'.format(self.value)
