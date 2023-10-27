# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.
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
    max_len = len(max(words_list, key=len, default=''))
    print('\n'.join(f'{indx:>3} {el:>{max_len}}' for indx, el in enumerate(words_list, 1)))


print_separated_words('А ещё многие известные личности подвергнуты целой серии\
независимых исследований. Приятно, граждане, наблюдать, как действия представителей\
оппозиции призывают нас к новым свершениям, которые, в свою очередь, должны\
быть объективно рассмотрены соответствующими инстанциями.')