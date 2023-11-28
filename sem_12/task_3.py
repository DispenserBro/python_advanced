# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self._stop = start
            self._start = 1
        else:
            self._start = start
            self._stop = stop
        self._step = step
    
    def __iter__(self):
        self.__prev_factorial = 1
        return self
    
    def __next__(self):
        while self._start < self._stop:
            self.__prev_factorial *= self._start
            self._start += self._step
            return self.__prev_factorial
        raise StopIteration('End of range reached')


for el in Factorial(7, 10):
    print(el)