# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# text = input.split()
RUS_ALPHA = tuple(chr(i) for i in range(1040, 1104)) + (chr(1025), chr(1105))

text = "Текст выравнивается по правому краю так, чтобы у самого длинного"
words = []
word = ''

for char in text.lower():
    if char.isalpha() or char in RUS_ALPHA:
        word += char
    else:
        words.append(word) if word else None
        word = ''

words.append(word) if word else None

words.sort()
print(words)
# words = sorted(words)

max_len = len(max(words, key=len))

for indx, el in enumerate(words):
    print(f"{indx+1:>3}. {el:>{max_len}}")
