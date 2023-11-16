# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

import os
import json
from typing import Callable


def save_result_to_json(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        path = 'results.json'
        
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                file_data = dict(json.load(f))
        else:
            file_data = {}
        
        
        result = func(*args, **kwargs)
        file_data[str(result)] = {'args': args}
        
        for key, value in kwargs.items():
            file_data[str(result)][key] = value
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, indent=2)

    return wrapper


@save_result_to_json
def return_args(*args, **kwargs):
    return args


return_args(1, 2, 3, 4, key='value')
