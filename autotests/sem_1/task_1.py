RUS_ALPHA = tuple(chr(i) for i in range(1040, 1104)) + (chr(1025), chr(1105))


def separate_words(text: str) -> list[str]:
    words = []
    word = ''

    for char in text.lower():
        if char.isalpha() or char in RUS_ALPHA:
            word += char
        else:
            words.append(word) if word else None
            word = ''

    words.append(word) if word else None

    return words


def print_separated_words(text: str) -> None:
    # words_list = separate_words(text)
    words_list = sorted(separate_words(text))
    max_len = len(max(words_list, key=len, default=0)) if words_list else 0
    print('\n'.join(f'{indx:>3} {el:>{max_len}}' for indx, el in enumerate(words_list)))


print_separated_words('Мы любим животных и стараемся поддерживать тех из них,\
кому не посчастливилось иметь ласковых хозяев и тёплый кров.\
Один из проверенных способов это сделать — помочь благотворительному фонду «Луч Добра».\
Благодаря их труду ежегодно сотни питомцев находят свой новый дом.')
