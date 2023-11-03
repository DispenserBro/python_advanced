# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

from random import randint
from sys import argv


def guess_number(guesses: int, lower_bound: int = 10, upper_bound: int = 20) -> None:
    current_guess = 1
    guessed_number = randint(lower_bound, upper_bound)

    while current_guess <= guesses:
        guess_num = int(input('Enter your guess: '))

        if guess_num == guessed_number:
            print('You win!!!')
            return True

        print(('больше', 'меньше')[guess_num > guessed_number])
        current_guess += 1

    print('You lose!')
    return False



if __name__ == "__main__":
    parsed_args = [int(arg) for arg in argv[1:]]

    guess_number(*parsed_args)