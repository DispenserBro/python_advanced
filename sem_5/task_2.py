# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку. 

from string import ascii_letters
from random import choice

dct = {i: ord(i) for i in ''.join(choice(ascii_letters) for i in range(10))}
