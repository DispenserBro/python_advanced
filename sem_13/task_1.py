# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def number_from_input() -> float | int:
    
    while True:
        try:
            value = input('Enter a number(integer or float): ')
            return int(value) if value.isdigit() else float(value)
        except ValueError:
            print('Please enter a number')


print(number_from_input())