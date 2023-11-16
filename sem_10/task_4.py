# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from datetime import date
from task_3 import Person
from random import randint


class Employee(Person):
    def __init__(
        self,
        name: str,
        patronymic: str,
        last_name: str,
        age: int,
        birth_date: date,
        uid: int = 0,
    ):
        super().__init__(name, patronymic, last_name, age, birth_date)
        self.id = uid if 1_000_000 > uid >= 100_000 else randint(100_000, 999_999)
        self.access_level = self.__get_access_level()

    def __get_access_level(self):
        return self.id % 7
    

person1 = Employee('Иван', 'Иванович', 'Иванов', 26, date(1996, 11, 16), 123456)
person2 = Employee('Иван', 'Иванович', 'Петров', 27, date(1995, 11, 16), 1)
person3 = Employee('Иван', 'Васильевич', 'Петров', 123, date(1900, 11, 16))

print(person1.id, person1.access_level, person1.full_name())
print(person2.id, person2.access_level, person2.full_name())
print(person3.id, person3.access_level, person3.full_name())



