# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию

_YEAR_BOUNDS = (1, 9999)


def _is_leap_year(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_possible_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if _YEAR_BOUNDS[0] <= year <= _YEAR_BOUNDS[1]:
        
        month_days = {
            1: 31, 2: (28, 29)[_is_leap_year(year)],
            3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

        if day in range(1, month_days.get(month, 0) + 1):
            return True
    
    return False

if __name__ == "__main__":
    print(is_possible_date('15.4.2023'))
    # print(is_possible_date('0.5.2022'))
    # print(is_possible_date('12.0.2022'))
    # print(is_possible_date('12.5.-2022'))
    print(is_possible_date('29.2.2020'))
    print(is_possible_date('12.5.2022'))
    print(is_possible_date('28.2.2021'))
    print(is_possible_date('31.12.9999'))
    # print(is_possible_date('12.13.2022'))
    # print(is_possible_date('29.2.2021'))
    # print(_is_leap_year(2021))
    # print(is_possible_date('30.2.2020'))