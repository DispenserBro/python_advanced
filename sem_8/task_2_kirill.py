import os
import json


def check_access_level(lvl: str) -> bool:
    return not (lvl.isdigit() and 0 < int(lvl) < 8)


def check_user_id(u_data: dict, u_id: int) -> bool:
    id_list = []
    for user in u_data.values():
        id_list.extend(user)
    return u_id in id_list


def main(file_path: str):
    users_data = {}
    if not os.path.exists(file_path):
        data = {}
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        with open(file_path, 'r', encoding='UTF-8') as file:
            users_data = json.load(file)

    while True:
        name = input('Введите имя пользователя или Enter для выхода: ')
        if not name:
            break
        u_id = int(input('Введите ID пользователя: '))
        while check_user_id(users_data, u_id):
            u_id = int(input(f'ID {u_id} уже занят, выберите другой ID: '))
        lvl_access = input('Введите уровень доступа пользователя: ')
        while check_access_level(lvl_access):
            lvl_access = input('Ошибка уровня доступа, введите число от 1 до 7: ')
        if lvl_access in users_data:
            users_data[lvl_access][u_id] = name
        else:
            users_data[lvl_access] = {u_id: name}
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump(users_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main('result.json')

