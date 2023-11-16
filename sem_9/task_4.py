# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable


def count_calls(calls: int) -> Callable:
    def deco(func: Callable) -> Callable:
        results = []
        def wrapper(*args, **kwargs):
            nonlocal results
            for _ in range(calls):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return deco
