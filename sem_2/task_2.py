# ✔Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔Избегайте магических чисел
# ✔Добавьте аннотацию типов где это возможно

BINARY_TUPLE = (0, 1)
OCTAL_TUPLE = (0, 1, 2, 3, 4, 5, 6, 7)
HEX_TUPLE = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

def convert_integer_to_number_system (value: int, number_system_tuple: tuple) -> str:
    result = ""
    num = value
    base = len(number_system_tuple)

    while (num > 0):
        result = str(number_system_tuple[num%base]) + result
        num //= base


    return result

print(convert_integer_to_number_system(255, HEX_TUPLE))