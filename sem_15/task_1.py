# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

from typing import Any
import logging

logging.basicConfig(filename='logs/log.log',
                    level=logging.WARNING,
                    # datefmt='%H:%M:%S',
                    format='[{levelname:<8}] {asctime}: {msg}',
                    style='{')
LOGGER = logging.getLogger(__name__)
# LOGGER.addHandler()

def get_from_dict(dct: dict, key: Any):
    try:
        return dct[key]
    except Exception as e:
        LOGGER.critical(f'Cannot get value from key: {key}, {e}')
        
dct = {
    1: '1',
    2: '2',
    3: '3',
}

get_from_dict(dct, 4)