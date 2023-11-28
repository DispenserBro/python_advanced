# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
# from random import choices

# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json

class Factorial:
    def __init__(self, k: int):
        self.k = k
        self._values_list = []
        self._results_list = []

    def _add_results(self, number: int, result: int):
        self._values_list.append(number)
        self._results_list.append(result)
        
        if len(self._results_list) > self.k:
            self._values_list = self._values_list[1:]
            self._results_list = self._results_list[1:]

    def _get_factorial(self, number: int) -> int:
        result = 1
        
        for i in range(2, number + 1):
            result *= i
        return result

    def __call__(self, number: int) -> int:
        result = self._get_factorial(number)
        self._add_results(number, result)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        with open ('results.json', 'w', encoding='utf-8') as f:
            json.dump(dict(zip(map(str, self._values_list), self._results_list)), f, indent=2)

    @property
    def results(self):
        return tuple(zip(self._values_list, self._results_list))


fact_1 = Factorial(3)

with fact_1:
    for i in range(1, 10):
        fact_1(int(i))
        for el in fact_1.results:
            print(f"Factorial of {el[0]} is {el[1]}")
        print('--------------------------------')