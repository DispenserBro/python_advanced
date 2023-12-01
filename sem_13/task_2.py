# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

from typing import Any


def new_dict_get(dct: dict, key: Any, default: Any = None):
    try:
        return dct[key]
    except KeyError:
        return default


dct_1 = {1: 'a', '2': (1, 2, 3)}

print(new_dict_get(dct_1, 1))
print(new_dict_get(dct_1, 3))
