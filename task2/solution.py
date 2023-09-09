import WikiAnimalParser as parser


def save_parse_result(result: dict) -> None:
    with open('beasts.csv', 'w', encoding='utf-8') as f:
        for value, cnt in result.items():
            f.write('{},{}\n'.format(value, cnt))

def main() -> None:
    with parser.WikiAnimalParser() as wiki_animal_parser:
        save_parse_result(wiki_animal_parser.get_result())

if __name__ == '__main__':
    main()
