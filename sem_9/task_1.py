# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


from random import randint
from typing import Callable


def guess_number_decorator(func: Callable) -> Callable:
    def wrapper(number_to_guess: int, guesses_count: int):
        func(number_to_guess if 0 < number_to_guess < 101 else randint(1, 100),
             guesses_count if 0 < guesses_count < 11 else randint(1, 10))
    
    return wrapper


@guess_number_decorator
def number_guess(number_to_guess: int, guesses_count: int):
    current_guess = 0
    
    while current_guess < guesses_count:
        print(f'Осталось {guesses_count - current_guess} попыток')
        guess = int(input('Введите ваше число: '))
        
        if guess == number_to_guess:
            print('Вы выиграли!')
            return
        
        current_guess += 1
        hints = [f'Больше, чем {guess}', f'Меньше, чем {guess}']
        print(hints[number_to_guess < guess])
    
    print(f'Вы проиграли! было загадо число {number_to_guess}')


guesser = number_guess(-1, -1)