import os
from random import randint, uniform

MIN_VALUE = -1000
MAX_VALUE = 1000


def file_creator(file_name: str, count: int):
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.write('')
    for _ in range(count):
        row = f'{randint(MIN_VALUE, MAX_VALUE)} | {uniform(MIN_VALUE, MAX_VALUE)}' + '\n'
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(row)


file_creator('example.txt', 5)