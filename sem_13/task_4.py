# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


import json
import os
from random import randint
from faker import Faker

from task_3 import AccessException

class AccessLevel:
    @classmethod
    def check_value(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a number')
        if not 7 >= value >= 1:
            raise AccessException('Access level must be in range [1, 7]')
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class User:
    access_level = AccessLevel()
    
    def __init__(self, name: str, u_id: int, access_level: int):
        self.name = name
        self.access_level = access_level
        self.u_id = u_id

    def __str__(self) -> str:
        return f'Пользователь: {self.name}, uid: {self.u_id}, уровень доступа: {self.access_level}'
    
    def __repr__(self) -> str:
        return f'User({self.name}, {self.u_id}, {self.access_level})'
    
    def __hash__(self) -> int:
        return hash(self.name) + hash(self.u_id) + hash(self.access_level)
    
    def __eq__(self, other:'User') -> bool:
        if hash(self) == hash(other):
            return True
        return self.name == other.name and self.u_id == other.u_id


class UsersGroup:
    def __init__(self, file_path):
        self.file_path = file_path
        self._users_data = self._get_u_data(self.file_path)
    
    def _check_uid(self, u_id: int) -> int:
        uid_list = [user.u_id for user in self._users_data]
        return u_id not in uid_list
    
    def add_user(self, u_name: str, u_id: int, u_access_level: int):
        if self._check_uid(u_id):
            self._users_data.append(User(u_name, u_id, u_access_level))
        # if 
    def save_u_data(self):
        data = {}
        for user in self._users_data:
            if user.access_level not in data:
                data[user.access_level] = {}
            data[user.access_level][user.u_id] = user.name
        
        with open(self.file_path, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    
    @staticmethod
    def _get_u_data(file_path: str) -> dict:
        u_data = []
        if not os.path.exists(file_path):
            users_data = {}
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
        else:
            with open(file_path, 'r', encoding='UTF-8') as file:
                users_data = json.load(file)
        for access_level in users_data:
            for uid in users_data[access_level]:
                u_data.append(User(users_data[access_level][uid], int(uid), int(access_level)))
        u_data.sort(key=lambda x: x.access_level)
        return u_data
    
    def __str__(self) -> str:
        return str(self._users_data)


fake = Faker('ru_RU')
group_1 = UsersGroup('users.json')
print(group_1)

for _ in range(randint(10, 20)):
    group_1.add_user(fake.name(), fake.unique.random_int(), randint(1, 7))

print(group_1)
group_1.save_u_data()
