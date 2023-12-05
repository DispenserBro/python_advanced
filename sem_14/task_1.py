# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import doctest
from string import ascii_lowercase

ALLOWED_LETTERS = ascii_lowercase + ' '

def filter_string(string: str) -> str:
    """
    >>> filter_string('abc')
    'abc'
    >>> filter_string('Abc')
    'abc'
    >>> filter_string('a.b.c')
    'abc'
    >>> filter_string('abcабв')
    'abc'
    >>> filter_string('Hello, мир!')
    'hello '
    """
    return ''.join(filter(lambda x: x in ALLOWED_LETTERS, string.lower()))


# print(filter_string('abc абв >b'))

if __name__ == "__main__":
    doctest.testmod(verbose=True)
