# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from datetime import date, datetime
import logging
import argparse

WEEKDAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                    'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

logging.basicConfig(filename='logs/log.log',
                    level=logging.NOTSET,
                    # datefmt='%H:%M:%S',
                    format='[{levelname:<8}] {asctime}: {funcName} -> {msg}',
                    style='{')
LOGGER = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description='Преобразование странной строки в дату')
parser.add_argument('-w', metavar='W', help='номер повтора дня недели', default=1)
parser.add_argument('-d', metavar='D', help='день недели числом или названием на русском', default=date.today().weekday())
parser.add_argument('-m', metavar='M', help='Месяц порядковым номером или названием на русском', default=date.today().month)


def convert_to_date(formatted_date: str) -> date:
    week, weekday, month = formatted_date.split()
    week = int(week.split('-')[0])
    if int(week) > 5:
        LOGGER.error(f'Invalid date format. Expected week <= 5, got {week}')
        return
    if weekday.isdigit():
        weekday = int(weekday)
    else:
        weekday = WEEKDAYS.index(weekday)
    if month.isdigit():
        month = int(month)
    else:
        month = MONTHS.index(month) + 1
    
    first_month_day = datetime.strptime(f'1 {month} {date.today().year}', '%d %m %Y').date().weekday()
    month_day = (week - 1) * 7 + weekday - first_month_day + (1 if first_month_day < weekday else 8)
    if month_day > 31:
        LOGGER.info(f"Invalid month week: {week}, month_day: {month_day} > 31")
        return
    return datetime.strptime(f'{month_day} {month} {date.today().year}', '%d %m %Y').date()


# print(convert_to_date('1-я вторник декабря'))
if __name__ == "__main__":
    args = parser.parse_args()
    print(convert_to_date(f'{args.w} {args.d} {args.m}'))