# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from datetime import date


class Person:
    def __init__(self, name: str, patronymic: str, last_name: str, age: int, birth_date: date):
        self.name = name
        self.patronymic = patronymic
        self.last_name = last_name
        self._age = age
        self._birth_date = birth_date
    
    @property
    def age(self):
        return self._age

    def birtday(self):
        if date.today() == self._birth_date:
            self._age += 1
    
    def full_name(self) -> str:
        return ' '.join([self.name, self.patronymic, self.last_name])


person1 = Person('Иван', 'Иванович', 'Иванов', 26, date(1996, 11, 16))
person1.birtday()
person1.full_name()

