# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

from functools import wraps
import sys
from typing import Callable
import logging


logging.basicConfig(filename='logs/log.log',
                    level=logging.NOTSET,
                    # datefmt='%H:%M:%S',
                    format='[{levelname:<8}] {asctime}: {funcName} -> {msg}',
                    style='{')
LOGGER = logging.getLogger(__name__)


def log(func: Callable) -> Callable:
    logger = logging.getLogger(func.__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        logger.info(f'{args=}, {kwargs=}, {result=}')
    return wrapper


@log
def add_numbers(*args, **kwargs):
    return sum(args)


add_numbers(1, 2, 10, 15, a=1, b=2, c=3)